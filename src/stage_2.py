import math
from select import select

from fontTools.subset import neuter_lookups
from sympy.logic.inference import valid

from stage_0 import *
from stage_1 import *
import numpy as np





class CalculateBeam(Prepare_Loads):
    def __init__(self, load_dict, beam_geometry):
        super().__init__(load_dict, beam_geometry)


        self.matrix_eq, self.matrix_sum = [self.f_eq], []
        self.f_values, self.f_locations = self.forces_equation()


        self.momentum_equation()
        # self.result_f = self.calculate_matrix()
        # self.all_sorted_loads = self.all_sorted_loads_f()














    def forces_equation(self):

        # sumna poprečnih sila (F i preračunatih q)
        sum_f = 0
        f_values, f_locations = [], []

        for key in self.sorted_loads:

            if self.sorted_loads[key]["type"] == "F":
                f_values.append(-self.sorted_loads[key]["value"])
                f_locations.append(self.sorted_loads[key]["position"])
                sum_f -= self.sorted_loads[key]["value"]

            elif self.sorted_loads[key]["type"] == "q":
                f_values.append(-self.sorted_loads[key]["F_eqv"])
                f_locations.append(self.sorted_loads[key]["x_F_eqv"])
                sum_f -= self.sorted_loads[key]["F_eqv"]

        self.matrix_sum.append([sum_f])



        return f_values, f_locations




    def momentum_equation(self):

        # lokacije točaka gdje će se postaviti momentne jednadžbe ( u osloncima ),
        # te se u njima trebaju postaviti momentne jendadžbe

        m_locations = [value["location"] for key, value in self.support_dict.items() if value["z"] is True ]


        for i in self.support_dict:
            print(i)



        # ide po potrebnom broju momentnih jednadžbi i postavlja momentne jednadžbe
        for x_pos in range(self.num_of_M_eq):
            m_eq = [i - x_pos for i in m_locations]       # momentna jednadža u koeficijentima



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


    CalculateBeam(load_dict=loads_1, beam_geometry=beam_geometry_1)





""""

- u jednadžbu sila teba dodati var momenta i postaviti ga na nulu
- momentne jednadže treba postaviti po potrebnim točkama 

- sve to ubaciti u jednadžbu za sumu sila i momenata) 


"""
