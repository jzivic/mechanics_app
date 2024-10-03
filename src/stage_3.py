"""
crtanje grafova q
"""


import matplotlib.pyplot as plt
from stage_2 import *


class Diagrams_forces(CalculateBeam):

    def __init__(self, load_dict, beam_geometry):
        super().__init__(load_dict, beam_geometry)

        self.final_loads = HelpClass.divide_q_for_F_f(self.output_sorted_loads)
        self.q_coords = self.create_coordinates_f()

        self.plot_graph()

    def create_coordinates_f(self):
        diag_coords = {"z": [0], "q": [0]}
        sum_q = 0
        for key, value in self.final_loads.items():
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

        if diag_coords["z"][-1] != self.beam_geometry["length"][-1]:
            diag_coords["q"].append(0)
            diag_coords["z"].append(self.beam_geometry["length"][-1])

        return diag_coords



    def plot_graph(self):


        plt.plot(self.q_coords["z"], self.q_coords["q"])

        plt.show()



        # Plot the beam as a thick black line
        beam_length = self.beam_geometry["length"][-1]






# Increase the figure size to make the diagram larger
#         plt.figure(figsize=(12, 8))
#
#
#
#         # Plot the q load diagram
#         z = self.q_coords["z"]
#         q = self.q_coords["q"]
#         plt.plot(z, q, label='q load')
#
#         # Annotate each point with its (z, q) coordinates
#         for i, txt in enumerate(q):
#             plt.annotate(f'({z[i]}, {txt})', (z[i], q[i]))
#
#         plt.ylabel('Load (q)')
#         plt.title('Load Diagram')
#         plt.legend()
#
#         plt.show()
#









if __name__ == "__main__":

    Diagrams_forces(load_dict=loads_1, beam_geometry=beam_geometry_1)


