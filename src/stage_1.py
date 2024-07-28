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




class PrepareQ:
    def __init__(self, load_dict):
        self.load_dict = load_dict
        self.sorted_loads = self.sort_loads()

    def sort_loads(self):
        sorted_forces_loads: dict = dict(sorted(self.load_dict.items(), key=lambda x:
            x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))


        # decompose F and q into x and y components
        for dec in sorted_forces_loads:

            if sorted_forces_loads[dec]["type"] == "F":
                sorted_forces_loads[dec]["F_x"], sorted_forces_loads[dec]["F_y"] = (
                    HelpF.decompose_force( sorted_forces_loads[dec]["value"],
                                           sorted_forces_loads[dec]["angle"] ))

            if sorted_forces_loads[dec]["type"] == "q":
                sorted_forces_loads[dec]["q_x"], sorted_forces_loads[dec]["q_y"] = (
                    HelpF.decompose_force( sorted_forces_loads[dec]["value"],
                                           sorted_forces_loads[dec]["angle"]))

        f_loads = {key: value for key, value in sorted_forces_loads.items() if value.get("type") == "F"}
        q_loads = {key: value for key, value in sorted_forces_loads.items() if value.get("type") == "q"}


        for key in q_loads:
            x_start = sorted_forces_loads[key]["position"][0]
            x_end = sorted_forces_loads[key]["position"][1]

            x_in_q = [x_start]
            # if there is a F within q range
            x_in_q += [sorted_forces_loads[x]["position"]
                       for x in f_loads if x_start < f_loads[x]["position"] < x_end]
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







        sorted_loads = dict(sorted(sorted_forces_loads.items(),
                                   key=lambda x: x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))

        return sorted_loads






# PrepareAll(load_dict=loads_1)






if __name__ == "__main__":

    print("Ovo je represija")

    PrepareQ(load_dict=loads_1)