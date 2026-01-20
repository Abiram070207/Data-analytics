import numpy as np
# 1. Define a 1D array
array_1d = np.array([23, 1, 45, 34, 7, 15, 92, 5])
print("Original 1D Array:", array_1d)
# Sort the 1D array
sorted_1d = np.sort(array_1d)
print("Sorted 1D Array:", sorted_1d)
# 2. Define a 2D array
array_2d = np.array([[34, 23, 5], [12, 92, 7], [45, 1, 15]])
print("\nOriginal 2D Array:\n", array_2d)
# Sort the 2D array along rows
sorted_2d_row = np.sort(array_2d, axis=1)
print("\n2D Array Sorted Along Rows:\n", sorted_2d_row)
# Sort the 2D array along columns
sorted_2d_col = np.sort(array_2d, axis=0)
print("\n2D Array Sorted Along Columns:\n", sorted_2d_col)
# 3. Custom sorting for structured array
data = np.array(
 [
 (3, "apple"),
 (1, "banana"),
 (2, "cherry"),
 ],
dtype=[("id", int), ("name", "U10")],
)
# Sort by 'id'
sorted_by_id = np.sort(data, order="id")
print("\nStructured Array Sorted by 'id':\n", sorted_by_id)
# Sort by 'name'
sorted_by_name = np.sort(data, order="name")
print("\nStructured Array Sorted by 'name':\n", sorted_by_name)
# 4. Demonstrating argsort
print("\nOriginal 1D Array for argsort:", array_1d)
indices = np.argsort(array_1d)
print("Indices of Sorted Array:", indices)
sorted_using_indices = array_1d[indices]
print("Array Sorted Using Indices:", sorted_using_indices)