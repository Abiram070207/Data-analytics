# 1a) NumPy Program

# Aim:
# The aim of a NumPy program in data analytics is to efficiently handle and process
# large datasets. It enables performing statistical computations, data transformations,
# and matrix operations.

# Algorithm:
# 1. Import NumPy
# 2. Create Array
# 3. Print Array Type
# 4. Check Dimensions
# 5. Check Shape
# 6. Check Size
# 7. Check Element Type

import numpy as np

# Step 2: Create Array
arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

# Step 3: Print Array Type
print("Array Type:", type(arr))

# Step 4: Check Dimensions
print("Dimensions (ndim):", arr.ndim)

# Step 5: Check Shape
print("Shape (rows x columns):", arr.shape)

# Step 6: Check Size
print("Total Elements (size):", arr.size)

# Step 7: Check Element Type
print("Element Data Type (dtype):", arr.dtype)
