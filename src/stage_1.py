"""
Stage 1 je dio koji će učitavati sile u neki riječnik gdje će biti svi podaci za jedan zadatak

# dodati da q može imati linearnu raspodjelu, a ne samo konst.


"""


from stage_0 import *



class HelpClass:
    def __init__(self):
        ...

    # continues load will be constant for now
    @staticmethod
    def transfor_q_to_F(q: dict):
        x1, x2 = q["position"][0], q["position"][1]     # beginning and finish
        f = q["value"] * (x2 - x1)       # equivalent force
        w_c = (x1 + x2) / 2                 # weight center

        return f, w_c


    @staticmethod
    def divide_q_for_F_f(loads_data):

        f_loads = {key: value for key, value in loads_data.items() if value.get("type") == "F"}
        q_loads = {key: value for key, value in loads_data.items() if value.get("type") == "q"}

        for key in q_loads:
            # dodaje se ekvivalentna sila koja može zamijeniti q, F_eqv, kao i njeno težište
            loads_data[key]["F_eqv"], loads_data[key]["x_F_eqv"] \
                = HelpClass.transfor_q_to_F(loads_data[key])

            x_start = loads_data[key]["position"][0]
            x_end = loads_data[key]["position"][1]

            # if there is a F within q range, x_in_q will store the location
            x_in_q = [x_start]

            # ako postoji neka sila F unutar kontinuiranog opterećenja dodaje se u x_in_q varijablu
            x_in_q += [loads_data[x]["position"] for x in f_loads if x_start < f_loads[x]["position"] < x_end]
            x_in_q.append(x_end)

            # dict u koji se dodaju
            dict_append = {}
            q_org = loads_data[key]

            num = 1
            for n in range(1, len(x_in_q)):
                range_q = [x_in_q[n - 1], x_in_q[n]]
                name = key + "_" + str(num)
                dict_append[name] = q_org.copy()
                dict_append[name]["position"] = range_q
                dict_append[name]["F_eqv"] = (range_q[1] - range_q[0]) * dict_append[name]["value"]
                dict_append[name]["x_F_eqv"] = range_q[0] + (range_q[1] - range_q[0]) / 2
                num += 1

            loads_data.pop(key)
            loads_data.update(dict_append)

        sorted_loads = dict(sorted(loads_data.items(),
                                   key=lambda x: x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))

        return sorted_loads




















class LinearEquation:
    def __init__(self, A, B, x):
        self.A = A
        self.B = B
        self.x = x
        self.result = self.compute_value()

        return ("Ovo je represija")

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







class Prepare_Loads:
    def __init__(self, load_dict, beam_geometry):

        self.load_dict = load_dict
        self.beam_geometry = beam_geometry

        # dict s osloncima reakcija
        self.support_dict = {key: value for key, value in beam_geometry.items() if key != "length"}
        # self.check_indeterminate()

        # jednadžba sila
        self.f_eq = [1] * len(self.support_dict.get("z", []))
        self.f_eq.extend([0] * len(self.support_dict.get("M", [])))
        self.num_of_M_eq = len(self.support_dict.get("z", [])) + len(self.support_dict.get("M", [])) - 1
        self.sorted_loads_specified = self.sort_decompose_loads()




    def check_indeterminate(self):
        n_supports = len(self.support_dict.get("z", [])) + len(self.support_dict.get("M", []))
        n_forces = len(self.load_dict)

        if n_supports > n_forces:
            raise ValueError("System is statistically undetermined")
        else:
            pass
            # print("System is ok")





    def sort_decompose_loads(self):

        # sve sile sortirane po poziciji. Ako je kont opterećenje, sorira se po prvoj dimenziji
        sorted_forces_loads = dict(sorted(self.load_dict.items(), key=lambda x:
            x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))

        sorted_data = HelpClass.divide_q_for_F_f(sorted_forces_loads)

        return sorted_data







if __name__ == "__main__":
    A = Prepare_Loads(load_dict=loads_1, beam_geometry=beam_geometry_1)

