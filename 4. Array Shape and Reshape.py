#Array shape and reshape
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.shape)  # Output: (2, 3)

arr1D = np.array([1, 2, 3, 4])
print(arr1D.shape)  # Output: (4,)

#1. Using reshape()
arr = np.arange(6)
reshaped = arr.reshape(2, 3)
print(reshaped)

#2. Converting Multi-Dimensional to 1D
matrix = np.array([[1, 2], [3, 4]])
flat = matrix.reshape(-1)
print(flat)  # Output: [1 2 3 4]

#Swap rows and columns using .T
matrix = np.array([[1, 2], [3, 4]])
print(matrix.T)

