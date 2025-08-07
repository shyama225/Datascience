import numpy as np

# Create a 4x4 array with random values
arr = np.random.rand(4, 4)
print("Original array:")
print(arr)

# Make a copy to avoid changing the original array
swapped_arr = arr.copy()

# Swap the first and last rows
swapped_arr[[0, -1]] = swapped_arr[[-1, 0]]

print("\nArray after swapping first and last rows:")
print(swapped_arr)
