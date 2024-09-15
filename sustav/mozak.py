# manim crtanje.py Crtanje_Momenta -pql

# from manim import *
# from elementi import *

from ulaz import *


beam = beam_1
delta = delta_1


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



class Calculate_Q():

    def __init__(self,  load_dict):
        self.load_dict = load_dict

        self.overall_sum = 0
        self.Q_coordinates = []

        self.prepare_load()
        self.main_function()
        self.Q_coordinates = self.remove_duplicates()

        # self.plot_Q()
        self.return_Q_coord()


    def prepare_load(self):

        sorted_loads_0: dict = dict(sorted(self.load_dict.items(), key=lambda x:
            x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))

        f_loads = {key: value for key, value in sorted_loads_0.items() if value.get("type") == "F"}
        q_loads = {key: value for key, value in sorted_loads_0.items() if value.get("type") == "q"}

        for key in q_loads:
            x_start = sorted_loads_0[key]["position"][0]
            x_end = sorted_loads_0[key]["position"][1]
            num = 2
            F_inters = [x for x in f_loads if x_start < f_loads[x]["position"] < x_end]
            x_in_q = [x_start]
            x_in_q += [sorted_loads_0[x]["position"] for x in f_loads if x_start < f_loads[x]["position"] < x_end]
            x_in_q.append(x_end)
            dict_append = {}
            q_org = sorted_loads_0[key]

            num = 1
            for n in range(1, len(x_in_q)):
                range_q = [x_in_q[n - 1], x_in_q[n]]
                name = key + "_" + str(num)
                dict_append[name] = q_org.copy()
                dict_append[name]["position"] = range_q
                num += 1

            sorted_loads_0.pop(key)
            sorted_loads_0.update(dict_append)


        self.sorted_loads = dict(sorted(sorted_loads_0.items(),
                   key=lambda x: x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))
        # self.f_loads = {key: value for key, value in self.sorted_loads.items() if value.get("type") == "F"}
        # self.q_loads = {key: value for key, value in self.sorted_loads.items() if value.get("type") == "q"}


    def main_function(self):
        for self.key in self.sorted_loads:
            type = self.sorted_loads[self.key]["type"]
            if type == "F":
                self.type_F()
            elif type == "q":
                self.type_q()



    def type_F(self):
        x = self.sorted_loads[self.key]["position"]
        F = self.sorted_loads[self.key]["amount"]

        print(x, F)

        k1 = [x, self.overall_sum]
        k2 = [x, self.overall_sum + F]
        self.Q_coordinates.__iadd__([k1, k2])
        # self.Q_coordinates.__iadd__((k1, k2))
        self.overall_sum += F



    def type_q(self):
        x_start = self.sorted_loads[self.key]["position"][0]
        x_end = self.sorted_loads[self.key]["position"][1]
        q = self.sorted_loads[self.key]["amount"]

        F = q*(x_end-x_start)
        k1 = [x_start, self.overall_sum]
        k2 = [x_end, self.overall_sum + F]
        self.Q_coordinates.__iadd__([k1, k2])
        self.overall_sum += F

    def remove_duplicates(self):
        seen = set()
        no_duplicates = [l for l in self.Q_coordinates if tuple(l) not in seen and not seen.add(tuple(l))]
        return no_duplicates

    def return_Q_coord(self):
        return self.Q_coordinates


Calculate_Q()


#####################################################################################
#####################################################################################


class Calculate_M(Calculate_Q):
    def __init__(self, load_dict, delta):

        self.delta = delta
        super().__init__(load_dict)

        self.step_list = []
        self.Moment_list = []
        self.prepare_M()
        self.return_M_coord_list()
        self.return_x_coord_list()

    def prepare_M(self):

        active_moments = list(filter(lambda item: item[1]["type"] == "M", self.sorted_loads.items()))
        moment_dict = {round(moment[1]["position"], 1): moment[1]["amount"] for moment in active_moments}
        M_in_0 = moment_dict[beam["start"]] if beam["start"] in moment_dict.keys() else 0
        

        mom_sum, moment_lists, step_lists = M_in_0, [], []
        for n in range(1, len(self.Q_coordinates)):
            A, B = self.Q_coordinates[n-1], self.Q_coordinates[n]

            if B[0] == A[0]: continue

            def slope_exception_handler(func):
                def wrapper(A, B):
                    if A[0] == B[0]:
                        return float('inf')
                    elif A[1] == B[1]:
                        return 0
                    else:
                        return func(A, B)
                return wrapper
            @slope_exception_handler
            def calculate_slope(A, B):
                return (B[1] - A[1]) / (B[0] - A[0])

            f = lambda x: calculate_slope(A=A, B=B) * (x - A[0]) + A[1]
            triangle = 0 if A[1] == B[1] else abs(0.5 * (f(self.delta)-f(0)) * self.delta)
            s_l = [A[0], A[0]] if len(step_lists) == 0 else [step_lists[-1][-1]]
            m_l = [0, M_in_0] if len(moment_lists) == 0 else [moment_lists[-1][-1]]

            for step in np.arange(A[0], B[0], self.delta):
                step += self.delta
                rounded_step = round(step, 2)

                mom_delta = f(step) * self.delta + triangle if f(step) <= f(step-self.delta) else f(step) * self.delta - triangle
                mom_sum += mom_delta

                if rounded_step in moment_dict:
                    s_l.append(round(step, 2))
                    m_l.append(round(mom_sum, 2))
                    step_lists.append(s_l)
                    moment_lists.append(m_l)

                    s_l = [A[0]] if len(step_lists) == 0 else [step_lists[-1][-1]]
                    m_l = [0] if len(moment_lists) == 0 else [moment_lists[-1][-1]]
                    step_lists.append([step, step])
                    moment_lists.append([mom_sum, mom_sum+moment_dict[rounded_step]])

                    mom_sum += moment_dict[rounded_step]
                    s_l = [A[0]] if len(step_lists) == 0 else [step_lists[-1][-1]]
                    m_l = [0] if len(moment_lists) == 0 else [moment_lists[-1][-1]]

                    continue

                s_l.append(round(step, 2))
                m_l.append(round(mom_sum, 2))

            step_lists.append(s_l)
            moment_lists.append(m_l)

        self.step_list = step_lists
        self.Moment_list = moment_lists

    def return_M_coord_list(self):
        return self.Moment_list

    def return_x_coord_list(self):
        return self.step_list


        # for n in range(len(step_lists)):
        #     plt.scatter(step_lists[n], moment_lists[n])
        # plt.show()
