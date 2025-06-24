#Array Indexing and Slicing
import numpy as np 
arr=np.array([10, 20, 30, 40, 50])
print(arr[2]) #Accessing the third element (index 2)

# Slicing the array to get elements from index 1 to 3 (exclusive of 4)
sliced_arr = arr[1:4]
print("Sliced Array:", sliced_arr)  # Output: [20 30 40]

# Slicing with a step
step_sliced_arr = arr[0:5:2]  # Start at index
# 0, stop before index 5, step by 2
print("Step Sliced Array:", step_sliced_arr)  # Output: [10 30 50]

#2D Array Indexing and Slicing

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", arr_2d)

# Accessing a specific element (row 1, column 2)
print("Element at (1, 2):", arr_2d[1, 2])  # Output: 6

# Slicing a 2D array to get the first two rows and first two columns
sliced_2d = arr_2d[:2, :2]
print("Sliced 2D Array:\n", sliced_2d)  

#Boolean Indexing
arr_bool=np.array([5,10,15,20,25])
# Boolean indexing to get elements greater than 15

print("Elements greater than 15:", arr_bool[arr_bool > 15])  # Output: [20 25]

#fancy indexing

print("Fancy Indexing:")
print(arr_bool[[0, 2, 4]])  # Output: [ 5 15 25]