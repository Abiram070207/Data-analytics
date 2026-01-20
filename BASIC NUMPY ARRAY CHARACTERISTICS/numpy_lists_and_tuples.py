import numpy as np
# 1. Creating a numpy array from a Python list
list_array = np.array([1.5, 2.5, 3.5], dtype=float)
print("Numpy Array from List (float type):", list_array)
# 2. Creating a numpy array from a Python tuple
tuple_array = np.array((1, 2, 3), dtype=int)
print("Numpy Array from Tuple (int type):", tuple_array)
# 3. Creating a numpy array with all zeros
zeros_array = np.zeros((3, 3), dtype=float)
print("Numpy Array of Zeros (3x3):\n", zeros_array)
# 4. Creating a numpy array with complex numbers
complex_array = np.array([1 + 2j, 3 + 4j, 5 + 6j], dtype=complex)
print("Numpy Array with Complex Numbers:", complex_array)
# 5. Creating a numpy array with random numbers
random_array = np.random.random((2, 3))
print("Numpy Array with Random Numbers (2x3):\n", random_array)
# 6. Creating a sequence of integers using np.arange()
arange_array = np.arange(10, 21, 2) # Start from 10, end before 21, step 2
print("Numpy Array with arange():", arange_array)
# 7. Creating a sequence of evenly spaced numbers using np.linspace()
linspace_array = np.linspace(0, 1, 5) # 5 evenly spaced numbers between 0 and 1
print("Numpy Array with linspace():", linspace_array)
# 8. Reshaping a numpy array
reshaped_array = np.arange(1, 13).reshape(3, 4) # 3 rows, 4 columns
print("Reshaped Numpy Array (3x4):\n", reshaped_array)
# 9. Flattening a numpy array
flattened_array = reshaped_array.flatten()
print("Flattened Numpy Array:", flattened_array)