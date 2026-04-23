
# Create numpy array of (3,3) dimension. Now find sum of all rows & columns individually. Also find 2nd maximum element in the array. 

import numpy as np

# Create a 3x3 NumPy array
arr = np.array([[3, 8, 1],
                [4, 6, 9],
                [7, 2, 5]])

print("Array:\n", arr)

# Sum of rows
row_sum = np.sum(arr, axis=1)
print("Sum of each row:", row_sum)

# Sum of columns
col_sum = np.sum(arr, axis=0)
print("Sum of each column:", col_sum)

sorted_arr = np.sort(arr, axis=None)
second_max = sorted_arr[-2]

print("Second maximum element:", second_max)