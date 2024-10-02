"""
crtanje grafova q
"""
from src_2.stage_0 import beam_geometry
from stage_2 import *


class Diagrams_forces(CalculateBeam):

    def __init__(self, load_dict, beam_geometry):
        super().__init__(load_dict, beam_geometry)

        self.proba()





    def proba(self):



        q_loads = {key: value for key, value in self.output_sorted_loads.items() if value.get("type") == "q"}





        diag_coords = { "z":[0], "q":[0] }

        sum_q = 0
        for key, value in self.output_sorted_loads.items():
            print(key)

            if value["type"] == "F":
                diag_coords["z"].append(value["position"])
                sum_q += value["value"]
                diag_coords["q"].append(sum_q)


            elif value["type"] == "q":
                diag_coords["z"].append(value["position"][0])
                diag_coords["q"].append(sum_q)

                diag_coords["z"].append(value["position"][1])
                sum_q += value["F_eqv"]
                diag_coords["q"].append(sum_q)


        # if diag_coords["z"][-1] != beam_geometry["length"][-1]:
        #     diag_coords["q"].append(0)
        #     diag_coords["z"].append(beam_geometry["length"][-1])







        print()











if __name__ == "__main__":

    Diagrams_forces(load_dict=loads_1, beam_geometry=beam_geometry_1)


