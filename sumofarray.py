import numpy as np

# Sample 2D array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Sum of all elements
total_sum = np.sum(arr)

# Sum of each column (axis=0)
col_sum = np.sum(arr, axis=0)

# Sum of each row (axis=1)
row_sum = np.sum(arr, axis=1)

print("Array:")
print(arr)
print("\nSum of all elements:", total_sum)
print("Sum of each column:", col_sum)
print("Sum of each row:", row_sum)
