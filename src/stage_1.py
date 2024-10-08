"""
Stage 1 je dio koji će učitavati sile u neki riječnik gdje će biti svi podaci za jedan zadatak

# dodati da q može imati linearnu raspodjelu, a ne samo konst.


"""

import math
from stage_0 import *



class HelpF:
    def __init__(self):
        ...

    @staticmethod
    def decompose_force(f_value, f_angle):
        f_y = - f_value * math.cos(math.radians(f_angle))
        f_x = - f_value * math.sin(math.radians(f_angle))

        return f_x, f_y

    # continues load will be constant for now
    @staticmethod
    def transfor_q_to_F(q: dict):
        x1, x2 = q["position"][0], q["position"][1]     # beginning and finish
        f = q["value"] * (x2 - x1)       # equivalent force
        w_c = (x1 + x2) / 2                 # weight center

        return f, w_c






class LinearEquation:
    def __init__(self, A, B, x):
        self.A = A
        self.B = B
        self.x = x
        self.result = self.compute_value()

    @staticmethod
    def slope_exception_handler(func):
        def wrapper(self):
            if self.A[0] == self.B[0]:
                return float('inf')
            elif self.A[1] == self.B[1]:
                return 0
            else:
                return func(self)
        return wrapper

    @slope_exception_handler
    def calculate_slope(self):
        return (self.B[1] - self.A[1]) / (self.B[0] - self.A[0])

    def compute_value(self):
        slope = self.calculate_slope()
        return slope * (self.x - self.A[0]) + self.A[1]

    def get_value(self):
        return self.result





















class Prepare_Q:
    def __init__(self, load_dict):
        self.load_dict = load_dict
        self.sorted_loads = self.sort_decompose_loads()

    def sort_decompose_loads(self):
        sorted_forces_loads = dict(sorted(self.load_dict.items(), key=lambda x:
            x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))


        # decompose F and q into x and y components
        for dec in sorted_forces_loads:

            # if sorted_forces_loads[dec]["type"] == "F":
            #     sorted_forces_loads[dec]["F_x"], sorted_forces_loads[dec]["F_y"] = (
            #         HelpF.decompose_force( sorted_forces_loads[dec]["value"],
            #                                sorted_forces_loads[dec]["angle"] ))

            if sorted_forces_loads[dec]["type"] == "q":
                # sorted_forces_loads[dec]["q_x"], sorted_forces_loads[dec]["q_y"] = (
                #     HelpF.decompose_force( sorted_forces_loads[dec]["value"],
                #                            sorted_forces_loads[dec]["angle"]))


                sorted_forces_loads[dec]["F_eq"], sorted_forces_loads[dec]["x_center"] \
                    = HelpF.transfor_q_to_F(sorted_forces_loads[dec])





        f_loads = {key: value for key, value in sorted_forces_loads.items() if value.get("type") == "F"}
        q_loads = {key: value for key, value in sorted_forces_loads.items() if value.get("type") == "q"}


        for key in q_loads:
            x_start = sorted_forces_loads[key]["position"][0]
            x_end = sorted_forces_loads[key]["position"][1]
            value = sorted_forces_loads[key]["value"]


            # if there is a F within q range, x_in_q will store the location
            x_in_q = [x_start]
            x_in_q += [sorted_forces_loads[x]["position"] for x in f_loads if x_start < f_loads[x]["position"] < x_end]
            x_in_q.append(x_end)
            dict_append = {}
            q_org = sorted_forces_loads[key]

            num = 1
            for n in range(1, len(x_in_q)):
                range_q = [x_in_q[n - 1], x_in_q[n]]
                name = key + "_" + str(num)
                dict_append[name] = q_org.copy()
                dict_append[name]["position"] = range_q
                num += 1

            sorted_forces_loads.pop(key)
            sorted_forces_loads.update(dict_append)


            f = value * (x_end - x_start)
            print(f)



        sorted_loads = dict(sorted(sorted_forces_loads.items(),
                                   key=lambda x: x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))

        return sorted_loads












if __name__ == "__main__":
    Prepare_Q(load_dict=loads_1)