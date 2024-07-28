import numpy as np


"""
    KONVENCIJA
    
    1. sile u osloncima gledaju gore, a sile od optrerećenja gledaju dolje na gredu




    Support će biti sile u osloncima i gledat će uvijek prema gore
    Forces je naznačen kao Lokacija: Iznos sile
    
    
"""







Data = {
    # "Beam": [0,6],              # Duljina grede
    "S": [2,5, 6],                 # Supports
    "F": {0:-2, 1:-1, 5:-5},          # Forces
}


# Fixed end


d_1 = {
    "Beam": [0,6],              # Duljina grede

    "S": [2,5, 6],                 # Supports
    


    "F": {0: -2, 1: -1, 5: -5},          # Forces




}








# za sada samo y smjer, samo sile
class SimpleBeam:

    def __init__(self):
        # print("Beam has been created")

        self.num_of_M_eq = len(Data["S"]) - 1           # broj potrebnnih momentnih jednadžbi

        self.Matrix_eq = []
        self.Matrix_sum = []


        self.forces_equation()
        self.momentum_equation()

        self.create_matrix()




    def forces_equation(self):

        F_eq = [1 for i in Data["S"]]          # linija u matrici sila za sumu sila u y smjeru
        self.Matrix_eq.append(F_eq)

        sum_F = [sum(Data["F"].values())]        # suma vanjskih sila
        self.Matrix_sum.append(sum_F)


    def momentum_equation(self):

        F_locations = list(Data["F"].keys())
        F_values = list(Data["F"].values())

        for n_equation in range(self.num_of_M_eq):
            x_pos = n_equation

            M_eq = [i-x_pos for i in Data["S"]]
            M_sum = [sum((i-x_pos)*j for i,j in zip(F_locations, F_values))]

            self.Matrix_eq.append(M_eq)
            self.Matrix_sum.append(M_sum)


        # print(self.Matrix_sum)
        # print(self.Matrix_eq)


    def create_matrix(self):

        # linearni način, nekad ima porblem sa singularnosti
        # Calculated_Forces = np.linalg.solve(self.Matrix_eq, self.Matrix_sum)


        # metoda najmanjih kvadrata
        X, residuals, rank, s = np.linalg.lstsq(self.Matrix_eq, self.Matrix_sum, rcond=None)

        print(X)


a = SimpleBeam()










