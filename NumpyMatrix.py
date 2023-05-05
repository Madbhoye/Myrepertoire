import numpy as np

A = [[2, 1, 1], [4, 3, 0]]
B = [[1, 2], [12, 0]]
C = [[1, 2], [12, 0], [-1, 2]]
D = [[1, 2, -4], [2, 0, 0], [1, 2, 3]]
E = np.bmat([[A, B], [C, D]]) # block matrix
type(E) # numpy.matrixlib.defmatrix.matrix

F = np.matrix(np.random.randn(5,5))
H = F*E # linear algebra product

B5 = np.linalg.matrix_power(B,5) # power
Bm1 = np.linalg.inv(B) # inverse
dB = np.linalg.det(B) # determinant
x = np.linalg.solve(B,[3,12])#solves B*x=[[3],[12]]