#Step 1: Define Grades
import numpy as np    
grades = np.array([72, 35, 64, 88, 51])

#Step 2: Calculate the Mean and Curve
avg = grades.mean()
adjusted_grades = grades + (80 - avg)

#Step 3: Clip the Values
#We want to ensure no grades go below the original or above 100.
final_grades = np.clip(adjusted_grades, grades, 100)
print(final_grades)
