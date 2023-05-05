import numpy as np
X = np.arange(start=5,step=3,stop=16) # 5, 8,11,14
A = np.ones((2,3)) # matrix filled with ones
B = X.reshape(2,2)
C = np.zeros((3,2)) # matrix filled with zeros
D = np.eye(2) # identity matrix
np.diag([1,2]) # diagonal matrix
E = C+np.ones(C.shape) # addition: same as C+1
F = B*D # entry-wise multiplication
J=np.dot(B,D) # linear algebra product
G = F.T # transpose matrix
H = np.exp(G) #as most functions, exp is entry-wise
#(else use np.vectorize(my_function))
x = np.array([4, 2, 1, 5, 1, 10])
y=np.logical_and(x>=3, x<= 9, x!=1) # [T,F,F,T,F,F]
x[y] # [4, 5]
print(np.mean(np.random.randn(1e5)>1.96)) 

