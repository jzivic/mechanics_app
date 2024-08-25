import math
from select import select

from sympy.logic.inference import valid

from stage_0 import *
from stage_1 import *
import numpy as np





class CalculateBeam:
    def __init__(self, sorted_loads):
        self.sorted_loads = sorted_loads

        # broj momentnih jednadžbi ovisi o broju oslonaca u y smjeru
        self.num_of_M_eq = len([1 for support in beam_geometry if support != "length"
                                and beam_geometry[support]["y"] is True]) - 1

        self.matrix_eq = []
        self.matrix_sum = []
        self.f_values, self.f_locations = self.forces_equation()
        self.momentum_equation()
        self.result_f = self.calculate_matrix()
        self.all_sorted_loads = self.all_sorted_loads_f()



    def forces_equation(self):

        f_eq = [1 for support in beam_geometry if support != "length" and
                beam_geometry[support]["y"] is True]
        self.matrix_eq.append(f_eq)

        # sumna poprečnih sila (F i preračunatih q)
        sum_q = 0
        f_values, f_locations = [], []
        for key in self.sorted_loads:

            if self.sorted_loads[key]["type"] == "F":
                f_values.append(-self.sorted_loads[key]["value"])
                f_locations.append(self.sorted_loads[key]["position"])
                sum_q -= self.sorted_loads[key]["value"]

            elif self.sorted_loads[key]["type"] == "q":
                f_values.append(-self.sorted_loads[key]["F_eqv"])
                f_locations.append(self.sorted_loads[key]["x_F_eqv"])
                sum_q -= self.sorted_loads[key]["F_eqv"]

        self.matrix_sum.append([sum_q])

        return f_values, f_locations


    def momentum_equation(self):

        # lokacije točaka gdje će se postaviti momentne jednadžbe ( u osloncima )
        locations = [value["location"] for key, value in beam_geometry.items() if key != "length"
                     and value["y"] is True ]

        # ide po potrebnom broju momentnih jednadžbi i postavlja momentne jednadžbe
        for x_pos in range(self.num_of_M_eq):
            m_eq = [i - x_pos for i in locations]       # momentna jednadža u koeficijentima
            self.matrix_eq.append(m_eq)

            m_sum = [sum((i-x_pos)*j for i,j in zip( self.f_locations, self.f_values))]
            self.matrix_sum.append(m_sum)

    def calculate_matrix(self):
        X, residuals, rank, s = np.linalg.lstsq(self.matrix_eq, self.matrix_sum, rcond=None)

        return X


    # vraća sve sile: q, F, R
    def all_sorted_loads_f(self):

        all_sorted_l = self.sorted_loads.copy()
        for n in range(len(self.f_locations) - 1):
            key = f'R{n + 1}'
            force = float(round(self.result_f[n][0], 3))
            location = self.f_locations[n]
            all_sorted_l[key] = {"type": "F", "value": force, "position": location, "angle": 0}

        all_sorted_loads = dict(sorted(all_sorted_l.items(), key=lambda x:
            x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))

        return all_sorted_loads










if __name__ == "__main__":
    processed_data = Prepare_Loads(loads_1).sorted_loads
    all_sorted_loads = CalculateBeam(sorted_loads=processed_data).all_sorted_loads

