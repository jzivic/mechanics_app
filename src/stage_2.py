import math
from stage_1 import *
from stage_0 import *




beam_geometry = {
        "length": [0,10],
        "S1": {"x": True, "y": True, "location": 0},
        "S2": {"x": True, "y": True, "location": 10}
}



class CalculateBeam:
    def __init__(self, loads):

        self.num_of_M_eq = len([1 for support in beam_geometry])-1
        self.Matrix_eq = []
        self.Matrix_sum = []
        self.forces_equation()




    def forces_equation(self):

        f_eq = [1 for support in beam_geometry if support != "length" and beam_geometry[support]["y"] == True]
        self.Matrix_eq.append(f_eq)


        # sum_F = [sum(Data["F"].values())
        # self.Matrix_sum.append(sum_F)









if __name__ == "__main__":
    processed_data = PrepareQ(loads_1).sorted_loads
    CalculateBeam(loads=processed_data)




