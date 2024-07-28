from sympy.physics.continuum_mechanics import Beam




Data_1 = {
    "Geometry": [0,6],              # Duljina grede
    "Support": [2,5, 6],                 # Supports
    "Forces": {0:-2, 1:-1, 5:-5},          # Forces
    "Moments": {5:5},          # Forces
}


class BeamSolver:


    def __init__(self, dict: Beam):

        print("Ovdje se trebaju rješavati jednačine")






    def Geometry(self):
        ...

    def Forces_x(self):
        ...

    def Forces_y(self):
        ...

    def Moments(self):
        ...






a = BeamSolver(Data_1)


help(print)