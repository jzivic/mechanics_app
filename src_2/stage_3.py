import math
from stage_0 import *
from stage_1 import *
from stage_2 import *
import numpy as np

import matplotlib.pyplot as plt




if __name__ == "__main__":
    processed_data = Prepare_Loads(loads_1).sorted_loads
    CalculateBeam(sorted_loads=processed_data)


    print(processed_data)
