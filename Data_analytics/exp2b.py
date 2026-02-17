import numpy as np

list_array = np.array([1.5, 2.5, 3.5], dtype=float)
print(list_array)

tuple_array = np.array((1, 2, 3), dtype=int)
print(tuple_array)

zeros_array = np.zeros((3, 3))
print(zeros_array)

complex_array = np.array([1+2j, 3+4j, 5+6j])
print(complex_array)

random_array = np.random.random((2, 3))
print(random_array)

arange_array = np.arange(10, 21, 2)
print(arange_array)

linspace_array = np.linspace(0, 1, 5)
print(linspace_array)

reshaped_array = np.arange(1, 13).reshape(3, 4)
print(reshaped_array)

flattened_array = reshaped_array.flatten()
print(flattened_array)
