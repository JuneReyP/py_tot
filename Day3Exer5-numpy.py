import numpy as np
#
# # define two matrices
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# # [1 2]   [5 6]   [1*5+2*7 1*6+2*8]
# # [3 4]   [7 8] = [3*5+4*7 3*6+4*8]
# #
# # Matrix multiplication
# C = np.dot(A, B)
# print("Matrix Multiplication:\n", C)

arr = np.array([[7,4,2],[9,5,6],[2,3,4]])
print("Original Array:")
print(arr)
# sort array
arr.sort()
print("Sorted Array:")
print(arr)