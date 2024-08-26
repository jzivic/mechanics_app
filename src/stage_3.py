import math
from stage_0 import *
from stage_1 import *
from stage_2 import *
import numpy as np

import matplotlib.pyplot as plt


class Diagrams_forces:

    def __init__(self, all_sorted_loads):


        for key, value in all_sorted_loads.items():

            v = value["value"]
            p = value["position"]

            print(p, v, key)













if __name__ == "__main__":
    processed_data = Prepare_Loads(loads_1).sorted_loads
    all_sorted_loads = CalculateBeam(sorted_loads=processed_data).all_sorted_loads


    Diagrams_forces(all_sorted_loads)

