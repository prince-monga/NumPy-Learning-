import numpy as np
arr = np.array([10, 20, 30, 40, 50])
filtered = arr[arr > 25]
print(filtered)  # Output: [30 40 50]

arr = np.array([5, 10, 15, 20, 25])
print(arr[(arr > 10) & (arr < 25)])  # Output: [15 20]

mask = arr > 10
print(mask)           # Output: [False False  True  True  True]
print(arr[mask])      # Output: [15 20 25]
