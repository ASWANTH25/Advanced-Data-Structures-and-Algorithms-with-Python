import numpy as np

# 1. Broadcasting
print("=== BROADCASTING ===")
A = np.array([[1, 2, 3],
              [4, 5, 6]])
B = np.array([10, 20, 30])

# B is broadcast to match A's shape
result = A + B
print("Broadcasting result:\n", result)

# 2. Universal Functions (ufunc)
print("\n=== UNIVERSAL FUNCTIONS ===")
arr = np.array([1, 4, 9, 16, 25])

# Custom ufunc
def custom_square(x):
    return x ** 2 + 2*x + 1

custom_ufunc = np.frompyfunc(custom_square, 1, 1)
result = custom_ufunc(arr)
print("Custom ufunc result:", result)

# 3. Masked Arrays
print("\n=== MASKED ARRAYS ===")
import numpy.ma as ma

data = np.array([1, 2, -999, 4, 5])  # -999 represents missing data
masked_data = ma.masked_where(data == -999, data)
print("Masked array:", masked_data)
print("Compressed (valid) data:", masked_data.compressed())

# 4. Structured Arrays
print("\n=== STRUCTURED ARRAYS ===")
# Creating arrays with different data types
dtype = [('name', 'U10'), ('age', 'i4'), ('height', 'f4')]
people = np.array([('Alice', 25, 5.5), ('Bob', 30, 6.0), ('Charlie', 35, 5.8)], dtype=dtype)
print("Structured array:", people)
print("Names:", people['name'])
print("Ages:", people['age'])
