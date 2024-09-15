import sympy

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
        self.f_values, self.f_locations = self.forces_equation()  # This adds the sum of forces first!
        self.equilibrium_equations()  # Then we add the moment equations

        # Solve the system of equations
        # self.result_f = self.calculate_matrix()

        # Sort all loads including the reaction forces
        # self.all_sorted_loads = self.all_sorted_loads_f()


    # Give names to the unknown reaction forces and moments at supports
    def naming_variables(self):
        variables = {}
        for n in range(len(self.support_dict.get("z", []))):
            variables[f'R{n + 1}'] = {"type": "F", "location": self.support_dict["z"][n], "value": None}
        for n in range(len(self.support_dict.get("M", []))):
            variables[f'M{n + 1}'] = {"type": "M", "location": self.support_dict["M"][n], "value": None}
        return variables


    def forces_equation(self):
        # Sum of applied forces (F and equivalent forces from distributed loads)
        sum_f = sum([v["value"] for v in self.sorted_loads.values() if v["type"] == "F"])


        f_values = []  # Store forces
        f_locations = []  # Store force positions

        for key, load in self.sorted_loads.items():
            if load["type"] == "F":  # Point force
                f_values.append(-load["value"])  # Negative for equilibrium
                f_locations.append(load["position"])
            elif load["type"] == "q":  # Distributed load (with equivalent force)
                f_values.append(-load["F_eqv"])  # Negative for equilibrium
                f_locations.append(load["x_F_eqv"])

        # Add the vertical equilibrium equation (∑F = 0) to the first row
        f_eq = [0] * len(self.variables)
        for i, (var_name, var_info) in enumerate(self.variables.items()):
            if var_info["type"] == "R":  # Reaction force
                f_eq[i] = 1  # Coefficient for reaction forces

        # Append the force equilibrium equation FIRST to the matrix
        self.matrix_eq.insert(0, f_eq)
        self.matrix_sum.insert(0, [sum_f])

        return f_values, f_locations






    def equilibrium_equations(self):

        sum_f = sum([v["value"] for v in self.sorted_loads.values() if v["type"] == "F"])
        sum_M = sum(v["value"] for v in self.sorted_loads.values() if v["type"] == "M")

        # Add moment equilibrium equations for each support
        m_locations = [var["location"] for var in self.variables.values() if var["type"] == "F"]

        # PRVO IDE JEDNADŽBA SILA
        # Loop through the support points to create moment equations

        a = []
        for key, value in self.variables.items():
            if value["type"] == "F":
                a.append()



        # for x_pos in m_locations:
        #     m_eq = [0] * len(self.variables)  # Moment equation
        #     total_moment_sum = 0  # Total moment sum
        #
        #     # Reaction force moments
        #     for i, (var_name, var_info) in enumerate(self.variables.items()):
        #         if var_info["type"] == "R":  # Reaction force
        #             dist = var_info["location"] - x_pos
        #             m_eq[i] = dist  # Moment arm
        #         elif var_info["type"] == "M":  # Reaction moment
        #             m_eq[i] = 1 if var_info["location"] == x_pos else 0
        #
        #
        #
        #
        #
        #     # Moments due to applied forces and distributed loads
        #     for f_loc, f_value in zip(self.f_locations, self.f_values):
        #         dist = f_loc - x_pos
        #         total_moment_sum += dist * f_value
        #
        #     # Add external moments to the sum
        #     total_moment_sum += ext_M_sum
        #
        #     # Append the moment equation and its sum to the matrix
        #     self.matrix_eq.append(m_eq)
        #     self.matrix_sum.append([total_moment_sum])
        #
        # print(f"Matrix Eq: {self.matrix_eq}")
        # print(f"Matrix Sum: {self.matrix_sum}")


    def calculate_matrix(self):
        # Solve the system of linear equations Ax = B
        matrix_eq_np = np.array(self.matrix_eq)
        matrix_sum_np = np.array(self.matrix_sum)

        # Solve using least squares (for overdetermined or exactly determined systems)
        X, residuals, rank, s = np.linalg.lstsq(matrix_eq_np, matrix_sum_np, rcond=None)
        print(f"Solved Forces and Moments: {X}")

        return X


    # Returns all forces: q, F, R
    def all_sorted_loads_f(self):
        all_sorted_l = self.sorted_loads.copy()
        for n in range(len(self.result_f)):
            key = f'R{n + 1}'
            if key in self.variables:  # Check if Rn exists in self.variables
                force = float(round(self.result_f[n][0], 3))
                location = self.variables[key]["location"]
                all_sorted_l[key] = {"type": "F", "value": force, "position": location, "angle": 0}

        # Sort all loads by position
        all_sorted_loads = dict(sorted(all_sorted_l.items(), key=lambda x: x[1]["position"]))

        return all_sorted_loads


if __name__ == "__main__":
    # Example inputs for loads and beam geometry
    CalculateBeam(load_dict=loads_1, beam_geometry=beam_geometry_1)
