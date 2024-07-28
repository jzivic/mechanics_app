import numpy as np

# Define the coefficient matrix A
A = np.array([
    [1, 1, 1],
    [2, 5, 6],
    [1, 4, 5]
])

# Define the constants matrix B
B = np.array([-8, -26, -18])

# Solve the system of equations
# X = np.linalg.solve(A, B)

print("Solution X:")
# print(X)


X, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)



print(X)