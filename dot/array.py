import numpy as np
A = np.array([1,2,3,4,5])
print (A.shape, A.ndim)

A = np.array([[1,2,3], [4,5,6]])
print(A.shape, A.ndim)

B = np.array([[1,2], [3,4], [5,6]])
print(B.shape, B.ndim)

#A*B 행렬 곱
print(np.dot(A,B))