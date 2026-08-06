# ==========================
# NUMPY QUICK REVISION SHEET
# ==========================

import numpy as np

# --------------------------------------------------
# 1. Creating Arrays
# --------------------------------------------------

arr1 = np.array([1, 2, 3, 4])                    # 1D Array
arr2 = np.array([[1, 2], [3, 4]])               # 2D Array
arr3 = np.array([[[1, 2], [3, 4]]])             # 3D Array

# --------------------------------------------------
# 2. Special Arrays
# --------------------------------------------------

np.zeros((3, 4))       # Array of zeros
np.ones((2, 3))        # Array of ones

import numpy as np
np.eye(4)              # Identity matrix

np.full((2, 2), 10)    # Fill array with a value

np.arange(1, 10, 2)    # Start, Stop, Step
# Output: [1 3 5 7 9]

np.linspace(0, 10, 5)  # Evenly spaced numbers
# Output: [0.  2.5  5.  7.5 10.]

# --------------------------------------------------
# 3. Random Numbers
# --------------------------------------------------

np.random.rand(3)           # Random decimals (0 to 1)
np.random.randint(1, 10, 5) # Random integers
np.random.randn(5)          # Normal distribution
np.random.seed(42)          # Fix random values

# --------------------------------------------------
# 4. Array Information
# --------------------------------------------------

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr.ndim       # Number of dimensions
arr.shape      # Shape (rows, columns)
arr.size       # Total elements
arr.dtype      # Data type
arr.itemsize   # Bytes per element

# --------------------------------------------------
# 5. Indexing
# --------------------------------------------------

arr[0]         # First row
arr[-1]        # Last row
arr[1, 2]      # Row 2, Column 3

# --------------------------------------------------
# 6. Slicing
# --------------------------------------------------

arr[0:2]       # Rows 0 to 1
arr[:, 1]      # Second column
arr[1, :]      # Second row
arr[:, :]      # Entire array

# --------------------------------------------------
# 7. Reshaping
# --------------------------------------------------

a = np.arange(6)

a.reshape(2, 3)   # Change shape
a.flatten()       # Copy into 1D
a.ravel()         # View into 1D (if possible)

# --------------------------------------------------
# 8. Arithmetic Operations
# --------------------------------------------------

arr + 5
arr - 2
arr * 3
arr / 2

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

a + b
a - b
a * b
a / b

# --------------------------------------------------
# 9. Mathematical Functions
# --------------------------------------------------

np.sqrt(arr)
np.square(arr)
np.exp(arr)
np.log(arr)
np.sin(arr)
np.cos(arr)
np.abs(arr)

# --------------------------------------------------
# 10. Aggregation Functions
# --------------------------------------------------

arr.sum()
arr.mean()
arr.max()
arr.min()
arr.std()
arr.var()

# --------------------------------------------------
# 11. Axis
# --------------------------------------------------

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

arr.sum(axis=0)    # Column-wise sum -> [5 7 9]
arr.sum(axis=1)    # Row-wise sum -> [6 15]

arr.mean(axis=0)
arr.max(axis=1)

# --------------------------------------------------
# 12. Sorting
# --------------------------------------------------

np.sort(arr)
np.argsort(arr)

# --------------------------------------------------
# 13. Boolean Filtering
# --------------------------------------------------

arr > 3
arr[arr > 3]

arr[(arr > 2) & (arr < 6)]
arr[(arr == 2) | (arr == 6)]

# --------------------------------------------------
# 14. Joining Arrays
# --------------------------------------------------

a = np.array([[1, 2]])
b = np.array([[3, 4]])

np.concatenate((a, b))
np.vstack((a, b))
np.hstack((a, b))

# --------------------------------------------------
# 15. Splitting Arrays
# --------------------------------------------------

arr = np.arange(8)

np.split(arr, 2)

arr2 = np.array([[1,2],[3,4],[5,6],[7,8]])

np.vsplit(arr2, 2)
np.hsplit(arr2, 2)

# --------------------------------------------------
# 16. Copy vs View
# --------------------------------------------------

copy_arr = arr.copy()    # Independent copy
view_arr = arr.view()    # Shares memory

# --------------------------------------------------
# 17. Transpose
# --------------------------------------------------

arr = np.array([[1,2,3],
                [4,5,6]])

arr.T
np.transpose(arr)

# --------------------------------------------------
# 18. Matrix Multiplication
# --------------------------------------------------

a = np.array([[1,2],[3,4]])

b = np.array([[5,6],[7,8]])

np.dot(a, b)
a @ b

# --------------------------------------------------
# 19. Useful Functions
# --------------------------------------------------

np.unique(arr)
np.unique(arr, return_counts=True)

np.argmax(arr)
np.argmin(arr)

# --------------------------------------------------
# 20. Broadcasting
# --------------------------------------------------

arr = np.array([1,2,3])

arr + 10
arr * 2

a = np.array([[1],[2],[3]])

b = np.array([10,20,30])

a + b

# Output:
# [[11 21 31]
#  [12 22 32]
#  [13 23 33]]

# --------------------------------------------------
# 21. Shape Changing
# --------------------------------------------------

arr = np.arange(6)

arr.reshape(3,2)
arr.resize((3,2))
arr.flatten()
arr.ravel()

# --------------------------------------------------
# 22. Frequently Asked Differences
# --------------------------------------------------

# reshape()  -> Returns reshaped array (doesn't modify original)
# resize()   -> Modifies original array

# flatten()  -> Returns COPY
# ravel()    -> Returns VIEW (if possible)

# copy()     -> Independent memory
# view()     -> Shared memory

# arange()   -> Specify step size
# linspace() -> Specify number of values

# --------------------------------------------------
# 23. Most Used NumPy Functions (AI / Data Science)
# --------------------------------------------------

# np.array()
# np.zeros()
# np.ones()
# np.eye()
# np.full()
# np.arange()
# np.linspace()
# np.random.rand()
# np.random.randint()
# np.random.randn()
# np.random.seed()
# reshape()
# flatten()
# ravel()
# transpose() / .T
# np.dot() / @
# sum()
# mean()
# max()
# min()
# std()
# var()
# unique()
# argmax()
# argmin()
# Boolean Indexing
# concatenate()
# vstack()
# hstack()