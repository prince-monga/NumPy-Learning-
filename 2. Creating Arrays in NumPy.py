import numpy as np 
arr1=np.array([10,20,30])

print("Array 1:", arr1)
# tuple array
tuple_array=np.array((5,10,15))
print("Tuple Array:", tuple_array)

#using predifune Function

#A. Zeros- Creaete an array filled with zeros
zeros_array = np.zeros((2, 3))  # 2 rows, 3 columns
print("Zeros Array:\n", zeros_array)

#B. Ones- Create an array filled with ones
ones_array=np.ones((2,2))   # 2 rows, 2 columns
print("Ones Array:\n", ones_array)

#C. Empty- Create an empty array (values are uninitialized)
empty_array = np.empty((2, 2))  # 2 rows, 2 columns
print("Empty Array:\n", empty_array)

#D. Full- Create an array filled with a specific value
full_array = np.full((2, 2), 7)  # 2 rows
print("Full Array:\n", full_array)

#E. Identity- Create an identity matrix

identity_array = np.identity(3)  # 3x3 identity matrix
print("Identity Array:\n", identity_array)

#F. Eye- Create a 2D array with ones on the diagonal and zeros elsewhere
eye_array = np.eye(3)  # 3x3 identity matrix
print("Eye Array:\n", eye_array)

#3. Generating Ranges- use functions that create sequence of numbers

#A. Arange- Create an array with a range of values
arange_array = np.arange(0, 10, 2)  # Start at
# 0, stop before 10, step by 2
print("Arange Array:", arange_array)


#B. Linspace- Create an array with evenly spaced values over a specified range
space_arr=np.linspace(0,1,5)
print("Linspace Array:", space_arr)
