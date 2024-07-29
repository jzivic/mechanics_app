import math
from stage_1 import *
from stage_0 import *




beam_geometry = {
        "length": [0,10],
        "S1": {"x": True, "y": True, "location": 0},
        "S2": {"x": True, "y": True, "location": 10}
}



class CalculateBeam:
    def __init__(self, sorted_loads):

        print(sorted_loads)

        self.sorted_loads = sorted_loads

        # broj momentnih jednadžbi ovisi o broju oslonaca u y smjeru
        self.num_of_M_eq = len([1 for support in beam_geometry if support != "length"
                                and beam_geometry[support]["y"] is True]) - 1
        self.matrix_eq = []
        self.matrix_sum = []
        self.forces_equation()




    def forces_equation(self):

        f_eq = [1 for support in beam_geometry if support != "length" and beam_geometry[support]["y"] is True]
        self.matrix_eq.append(f_eq)

        # sumna poprečnih sila (F i preračunatih q)
        sum_Q = 0




        f_values, f_locations = [], []
        for key in self.sorted_loads:

            if self.sorted_loads[key]["type"] == "F":
                f_values.append(self.sorted_loads[key]["value"])
                f_locations.append(self.sorted_loads[key]["positions"])

                sum_Q += self.sorted_loads[key]["value"]

            elif self.sorted_loads[key]["type"] == "q":
                sum_Q += self.sorted_loads[key]["F_eqv"]

        self.matrix_sum.append(sum_Q)




    def momentum_equation(self):
        #kurton
        ...











"""


    Data = {
        # "Beam": [0,6],              # Duljina grede
        "S": [2, 5, 6],  # Supports
        "F": {0: -2, 1: -1, 5: -5},  # Forces
    }
    def momentum_equation(self):

        F_locations = list(Data["F"].keys())
        F_values = list(Data["F"].values())

        for n_equation in range(self.num_of_M_eq):
            x_pos = n_equation

            M_eq = [i-x_pos for i in Data["S"]]
            M_sum = [sum((i-x_pos)*j for i,j in zip(F_locations, F_values))]

            self.Matrix_eq.append(M_eq)
            self.Matrix_sum.append(M_sum)"""

















if __name__ == "__main__":
    processed_data = Prepare_Loads(loads_1).sorted_loads
    CalculateBeam(sorted_loads=processed_data)




