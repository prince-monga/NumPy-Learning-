import numpy as np  

# 1D Array
Arr1 = np.array([10, 20, 30, 40, 50])  # Creates a 1D array
print("1D Array:\n", Arr1, "\n")

# 2D Array
Arr2 = np.array([[10, 20], [30, 40]])  # Creates a 2D array (matrix)
print("2D Array:\n", Arr2, "\n")

# Zeros Array
Arr3 = np.zeros((3, 2))  # Creates a 3x2 array filled with 0s
print("Zeros Array:\n", Arr3, "\n")

# Ones Array
Arr4 = np.ones((3, 2))  # Creates a 3x2 array filled with 1s
print("Ones Array:\n", Arr4, "\n")

# Empty Array
Arr5 = np.empty((2, 3))  # Creates an uninitialized 2x3 array (random values)
print("Empty Array:\n", Arr5, "\n")

# Array with range
Arr6 = np.arange(1, 10, 2)  # Creates array from 1 to 9 with step 2
print("Array with arange:\n", Arr6, "\n")

# Equally spaced numbers
Arr7 = np.linspace(0, 1, 5)  # Creates 5 equally spaced values from 0 to 1
print("Equally Spaced Array:\n", Arr7, "\n")

# Identity Matrix
Arr8 = np.eye(3)  # Creates a 3x3 identity matrix
print("Identity Matrix:\n", Arr8, "\n")

# Full Array
Arr9 = np.full((2, 2), 99)  # Creates a 2x2 array filled with 99
print("Full Array:\n", Arr9, "\n")
# Random Array
Arr10 = np.random.rand(2, 3)  # Creates a 2x3 array with random values between 0 and 1
print("Random Array:\n", Arr10, "\n")