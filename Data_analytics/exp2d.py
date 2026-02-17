import numpy as np

array_1d = np.array([23, 1, 45, 34, 7, 15, 92, 5])
print("Sorted 1D:", np.sort(array_1d))

array_2d = np.array([[34, 23, 5], [12, 92, 7], [45, 1, 15]])

print("Sorted Rows:\n", np.sort(array_2d, axis=1))
print("Sorted Columns:\n", np.sort(array_2d, axis=0))

data = np.array(
    [(3, "apple"), (1, "banana"), (2, "cherry")],
    dtype=[("id", int), ("name", "U10")]
)

print(np.sort(data, order="id"))
print(np.sort(data, order="name"))

indices = np.argsort(array_1d)
print(array_1d[indices])
