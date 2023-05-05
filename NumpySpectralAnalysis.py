import numpy as np

A = [[1, 2], [12, 3]]
x = np.linalg.eigvals(A) # eigenvalues
# eigenvalues and eigenvectors:
valp, vectp = np.linalg.eig(A) 

#Hermitian matrices methods:
S = [[1, 2], [2, 3]]
y = np.linalg.eigvals(S) # eigenvalues
# eigenvalues and eigenvectors:
Valp, vVctp = np.linalg.eig(S)
  
#SVD:
U,s,V=np.linalg.svd(A)
Ap = np.matrix(U)*np.diag(s)*V
print(A-Ap)