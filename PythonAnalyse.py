import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
def f(x):
    return np.exp(x)+x
#zeros of f, computed starting at -0.2:
a=sp.optimize.fsolve(f,-.2) 
print(f(a))
#integral of f from 0 to 1:
b=sp.integrate.quad(f,0,1) 
def g(y,t):
    return y
T=np.arange(start=0,stop=1,step=.001)
#solution, at T, of y'=g(y,t) starting at 1 at T[0]:
y=sp.integrate.odeint(g,1,T)
plt.plot(T,np.log(y),"r")
plt.show()