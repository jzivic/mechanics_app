import sympy
from numpy.ma.testutils import fail_if_equal

from stage_0 import *
from stage_1 import *

import numpy as np

class CalculateBeam(Prepare_Loads):
    def __init__(self, load_dict, beam_geometry):
        super().__init__(load_dict, beam_geometry)

        self.variables = self.naming_variables()        # unknown reactions and moments


        # Initialize equation matrices for forces and moments
        self.matrix_eq = []  # Left-hand side (coefficients)
        self.matrix_sum = []  # Right-hand side (sums)

        # Calculate the equilibrium equations (force and moment) and solve
        self.result_matrix = self.equilibrium_equations()  # Then we add the moment equations

        # Sort all loads including the reaction forces
        self.all_sorted_loads = self.all_sorted_loads_f()


        print(3)



    # Give names to the unknown reaction forces and moments at supports
    def naming_variables(self):
        variables = {}
        for n in range(len(self.support_dict.get("z", []))):
            variables[f'R{n + 1}'] = {"type": "F", "position": self.support_dict["z"][n], "value": None}
        for n in range(len(self.support_dict.get("M", []))):
            variables[f'M{n + 1}'] = {"type": "M", "position": self.support_dict["M"][n], "value": None}
        return variables





    SAMO JOŠ OVO TREBA SREDITI I DRŽATI SE KONVENCIJE, NEGDJE KRIVO MNOŽI I ZBRAAJ MOMENTE

    def equilibrium_equations(self):

        sum_f = (sum([v["value"] for v in self.sorted_loads.values() if v["type"] == "F"]) +
                 sum([v["F_eqv"] for v in self.sorted_loads.values() if v["type"] == "q"]))

        matrix_sum = [[sum_f]]

        # PRVO IDE JEDNADŽBA SILA
        f_eq = [1 for v in self.variables.values() if v["type"] == "F"]
        f_eq.extend([0 for v in self.variables.values() if v["type"] == "M"])
        matrix_eq = [f_eq]

        # MOMNENTNA JEDNADŽBA
        sum_M_extern = -sum(v["value"] for v in self.sorted_loads.values() if v["type"] == "M")
        m_locations = [var["position"] for var in self.variables.values() if var["type"] == "F"]

        for x_pos in m_locations:
            sum_M_position = sum_M_extern

            m_eq = [None] * len(self.variables)  # Moment equation
            for n, (var_name, var_info) in enumerate(self.variables.items()):
                if var_info["type"] == "F":  # Reaction force
                    dist = var_info["position"] - x_pos
                    m_eq[n] = dist  # Moment arm
                elif var_info["type"] == "q":
                    dist = var_info["x_F_ewv"] - x_pos
                    m_eq[n] = dist
                elif var_info["type"] == "M":  # Reaction force
                    m_eq[n] = 1
            matrix_eq.append(m_eq)

            for key, value in self.sorted_loads.items():
                if value["type"] == "F":
                    sum_M_position -= value["value"] * (value["position"] - x_pos)
                elif value["type"] == "q":
                    sum_M_position -= value["value"] * (value["x_F_eqv"] - x_pos)
            matrix_sum.append([sum_M_position])

        X, residuals, rank, s = np.linalg.lstsq(matrix_eq, matrix_sum, rcond=None)

        for n, key in enumerate(self.variables):
            self.variables[key]['value'] = X[n][0]

        return X


    # Returns all forces: q, F, R
    def all_sorted_loads_f(self):

        all_loads = self.sorted_loads | self.variables
        sorted_loads = dict(sorted(all_loads.items(),
            key=lambda x: x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))

        return sorted_loads



if __name__ == "__main__":
    # Example inputs for loads and beam geometry
    CalculateBeam(load_dict=loads_1, beam_geometry=beam_geometry_1)
