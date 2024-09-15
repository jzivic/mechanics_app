
from stage_0 import *
from stage_1 import *
import numpy as np





class CalculateBeam(Prepare_Loads):
    def __init__(self, load_dict, beam_geometry):
        super().__init__(load_dict, beam_geometry)

        self.variables = self.naming_variables()
        self.matrix_eq, self.matrix_sum = [self.f_eq], []
        # self.f_values, self.f_locations = self.forces_equation()
        # self.momentum_equation()

        self.equilibrium_equations()


        # self.result_f = self.calculate_matrix()

        # self.all_sorted_loads = self.all_sorted_loads_f()



    # daje imena silama i momentima u osloncima
    def naming_variables(self):
        variables = {}
        for n in range(len(self.support_dict.get("z", []))):
            variables[f'R{n + 1}'] = {"type": "R", "location": self.support_dict["z"][n], "value": None}
        for n in range(len(self.support_dict.get("M", []))):
            variables[f'M{n + 1}'] = {"type": "M", "location": self.support_dict["M"][n], "value": None}

        return variables



    def forces_equation(self):
        # Sum of applied forces (F and equivalent forces from distributed loads)
        sum_f = 0
        f_values, f_locations = [], []

        # Loop through sorted loads and calculate the total force
        for key in self.sorted_loads:
            load = self.sorted_loads[key]

            if load["type"] == "F":  # Point force
                f_values.append(-load["value"])
                f_locations.append(load["position"])
                sum_f -= load["value"]

            elif load["type"] == "q":  # Distributed load (with equivalent force)
                f_values.append(-load["F_eqv"])
                f_locations.append(load["x_F_eqv"])
                sum_f -= load["F_eqv"]

        # Initialize the force equilibrium equation
        f_eq = [0] * len(self.variables)

        # Add reaction forces to the force equilibrium equation
        for i, (var_name, var_info) in enumerate(self.variables.items()):
            if var_info["type"] == "R":  # Reaction force
                f_eq[i] = 1  # Coefficient for the reaction force

        # Add the force equation to the system (∑F = 0)
        self.matrix_eq.append(f_eq)
        self.matrix_sum.append([sum_f])  # Total sum of forces must be zero

        print(f"Force Equation Added: {f_eq}")
        print(f"Force Sum: {sum_f}")

        return f_values, f_locations
    def momentum_equation(self):
        # Sum of external moments (with their respective locations)
        ext_M_sum = sum(v["value"] if v["type"] == "M" else 0 for v in self.sorted_loads.values())

        # Positions for moment equations (e.g., support locations)
        m_locations = [var["location"] for var in self.variables.values() if var["type"] == "R"]

        # Loop over the positions for moment equations
        for x_pos in m_locations:
            M_eq = []  # Stores coefficients for reaction moments
            total_moment_sum = 0  # Moment summation at x_pos

            # Add moments due to reaction forces at supports
            for var_name, var_info in self.variables.items():
                if var_info["type"] == "R":  # Reaction force
                    dist = var_info["location"] - x_pos
                    M_eq.append(dist)  # Add the moment arm coefficient
                elif var_info["type"] == "M":  # Moment reaction
                    M_eq.append(1 if var_info["location"] == x_pos else 0)

            # Add moments due to applied forces and distributed loads
            for f_loc, f_value in zip(self.f_locations, self.f_values):
                dist = f_loc - x_pos
                total_moment_sum += dist * f_value

            # Add external moments directly (if any)
            total_moment_sum += ext_M_sum

            # Append the equation to the matrix
            self.matrix_eq.append(M_eq)
            self.matrix_sum.append([total_moment_sum])

        print(f"Matrix Eq: {self.matrix_eq}")
        print(f"Matrix Sum: {self.matrix_sum}")






    def equilibrium_equations(self):
        # Initialize force equation (∑F = 0) and external moment sum (∑M)
        sum_f = 0
        ext_M_sum = 0

        # Initialize matrices for equilibrium equations
        f_eq = [0] * len(self.variables)  # For force equilibrium
        m_eq_list = []  # For moment equilibrium equations
        m_sum_list = []  # For moment sums

        # Loop through all sorted loads (applied forces and moments)
        for key, load in self.sorted_loads.items():
            if load["type"] == "F":  # Point force
                sum_f -= load["value"]  # Sum of forces
            elif load["type"] == "q":  # Distributed load (with equivalent force)
                sum_f -= load["F_eqv"]  # Sum of equivalent forces
            elif load["type"] == "M":  # External moment
                ext_M_sum += load["value"]  # Sum of moments

        # Add reaction forces to the force equilibrium equation (∑F = 0)
        for i, (var_name, var_info) in enumerate(self.variables.items()):
            if var_info["type"] == "R":  # Reaction force
                f_eq[i] = 1  # Coefficient for reaction forces

            elif var_info["type"] == "M":  # Reaction force
                f_eq[i] = "duljina poluge"

            print(var_info)




        # Append the force equilibrium equation (∑F = 0) to matrix
        self.matrix_eq.append(f_eq)
        self.matrix_sum.append([sum_f])

        # Moment equilibrium at support points
        m_locations = [var["location"] for var in self.variables.values() if var["type"] == "R"]

        # Calculate moment equilibrium equations for each support point
        for x_pos in m_locations:
            m_eq = [0] * len(self.variables)  # Initialize moment equation
            total_moment_sum = 0  # Moment summation at x_pos

            # Add reaction forces' contribution to moments
            for i, (var_name, var_info) in enumerate(self.variables.items()):
                if var_info["type"] == "R":  # Reaction force
                    dist = var_info["location"] - x_pos
                    m_eq[i] = dist  # Add moment arm to the equation
                elif var_info["type"] == "M":  # Reaction moment
                    m_eq[i] = 1 if var_info["location"] == x_pos else 0

            # Add contributions from applied forces and distributed loads
            for f_loc, f_value in zip(self.f_locations, self.f_values):
                dist = f_loc - x_pos
                total_moment_sum += dist * f_value

            # Add external moments (directly applied)
            total_moment_sum += ext_M_sum

            # Append the moment equation (∑M = 0) to matrix
            m_eq_list.append(m_eq)
            m_sum_list.append([total_moment_sum])

        # Append moment equilibrium equations to matrix_eq and matrix_sum
        self.matrix_eq.extend(m_eq_list)
        self.matrix_sum.extend(m_sum_list)

        print(f"Matrix Eq: {self.matrix_eq}")
        print(f"Matrix Sum: {self.matrix_sum}")











    def calculate_matrix(self):
        X, residuals, rank, s = np.linalg.lstsq(self.matrix_eq, self.matrix_sum, rcond=None)

        print(X)


        return X


    # vraća sve sile: q, F, R
    def all_sorted_loads_f(self):

        all_sorted_l = self.sorted_loads.copy()
        for n in range(len(self.f_locations) - 1):
            key = f'R{n + 1}'
            force = float(round(self.result_f[n][0], 3))
            location = self.f_locations[n]
            all_sorted_l[key] = {"type": "F", "value": force, "position": location, "angle": 0}

        all_sorted_loads = dict(sorted(all_sorted_l.items(), key=lambda x:
            x[1]["position"][0] if x[1]["type"] == "q" else x[1]["position"]))

        return all_sorted_loads










if __name__ == "__main__":


    CalculateBeam(load_dict=loads_1, beam_geometry=beam_geometry_1)



