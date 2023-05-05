import numpy as np

x = np.array([[8,3,2],[5,1,0],[9,7,1]])
y = x
x[0,0]+=1
x[0,0]-y[0,0] # 0
z=x.copy()
x[0,0]+=1
x[0,0]-z[0,0] # 1