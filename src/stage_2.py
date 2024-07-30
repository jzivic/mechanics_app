import math
from stage_1 import *
from stage_0 import *






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




    def forces_equation(self):

        f_eq = [1 for support in beam_geometry if support != "length" and beam_geometry[support]["y"] is True]
        self.matrix_eq.append(f_eq)

        # sumna poprečnih sila (F i preračunatih q)
        sum_Q = 0
        f_values, f_locations = [], []
        for key in self.sorted_loads:

            if self.sorted_loads[key]["type"] == "F":
                f_values.append(self.sorted_loads[key]["value"])
                f_locations.append(self.sorted_loads[key]["position"])
                sum_Q += self.sorted_loads[key]["value"]

            elif self.sorted_loads[key]["type"] == "q":
                f_values.append(self.sorted_loads[key]["F_eqv"])
                f_locations.append(self.sorted_loads[key]["x_F_eqv"])
                sum_Q += self.sorted_loads[key]["F_eqv"]

        self.matrix_sum.append(sum_Q)

        return f_values, f_locations



    def momentum_equation(self):


        # lokacije točaka gdje će se postaviti momentne jednadžbe ( u osloncima )
        locations = [value["location"] for key, value in beam_geometry.items() if key != "length"]



        # ide po potrebnom broju momentnih jednadžbi i postavlja momentne jednadžbe
        for x_pos in range(self.num_of_M_eq):
            M_eq = [i - x_pos for i in locations]
            M_sum = [sum((i-x_pos)*j for i,j in zip( self.f_locations, self.f_values))]


















if __name__ == "__main__":
    processed_data = Prepare_Loads(loads_1).sorted_loads
    CalculateBeam(sorted_loads=processed_data)


    # print(processed_data)


