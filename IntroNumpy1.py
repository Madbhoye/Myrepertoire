import numpy as np
b = np.array([[8,3,2,4],[5,1,6,0],[9,7,4,1]])
type(b) # numpy.ndarray
b.dtype # datatype: int
b.shape # (3,4)
c = np.array([[8,2],[5,6],[9,7]], dtype=complex)
c.dtype # datatype: complex
c[0,0] # 8+0j

#More than 2 dimensions:
d = np.array([[[8,3],[1,2]],[[5,1],[4,5]],[[9,7],[4,5]]])
d.shape # (3, 2, 2)
#Reshaping:
x = d.reshape(4,3) # tableau de taille (4,3)
d.reshape(12,1) # tableau de taille (12,1)
d.reshape(12,) # tableau unidimensionel de taille 12
np.insert(np.arange(4,9),3,17) # 4,5,6,17,7,8