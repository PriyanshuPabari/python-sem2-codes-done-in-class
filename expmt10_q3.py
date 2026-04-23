
# Perform Matrix multiplication of any 2 n*n matrices.

import numpy as np

# Define two n x n matrices (example: 3x3)
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix multiplication
result = np.dot(A, B)   # or A @ B

print("Result of Matrix Multiplication:\n", result)