import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

print(arr1 + arr2)   # [5 7 9]
print(arr1 - arr2)   # [-3 -3 -3]
print(arr1 * arr2)   # [4 10 18]
print(arr2 / arr1)   # [4.0 2.5 2.0]

#Mathematical Functions (ufuncs)
#1. Square Root
arr = np.array([4, 9, 16])
print(np.sqrt(arr))  # [2. 3. 4.]


#2. Exponentiation
arr = np.array([1, 2, 3])
print(np.exp(arr))  # [ 2.718  7.389  20.085 ]

#3. Logarithm
arr = np.array([1, np.e, np.e**2])
print(np.log(arr))  # [0. 1. 2.]

#Aggregate Functions

#Useful for summarizing data:
arr = np.array([1, 2, 3, 4])
print(arr.sum())       # 10
print(arr.mean())      # 2.5
print(arr.min())       # 1
print(arr.max())       # 4
print(arr.std())       # Standard deviation
