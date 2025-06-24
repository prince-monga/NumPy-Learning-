#Add Scalar to Array
import numpy as np
arr = np.array([10, 20, 30])
print(arr + 5)

#Add 1D Array to 2D Array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
row = np.array([10, 20, 30])
print(matrix + row)

#Broadcasting with Columns

col = np.array([[10], [20]])
print(matrix + col)
