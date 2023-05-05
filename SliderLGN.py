import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
plt.close("all")



NMin,NMax=1.,int(1e3)
alphamin,alphamax=.8,2.
signs = 2*np.random.binomial(1,.5,NMax)-1
U = np.random.rand(NMax)
t=np.arange(1,int(NMax)+1)

M=10#max(abs(np.cumsum(signs*U**(-1))/t))



fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
N0 = 500
alpha0=1.
X=signs[:N0]*U[:N0]**(-1/alpha0)
S=np.cumsum(X)/t[:N0]
plt.title("LGN: convergence ou pas selon alpha")
plt.plot((0,1),(0,0),"b--")
l,=plt.plot(t[:N0]/N0,S,"r",label="Moyenne empirique")
plt.axis([0, 1, -M,M])
ax.set_xticklabels(()) 
plt.xlabel("n")
plt.legend(loc=1)


axcolor = 'lightgoldenrodyellow'
axN = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)
axalpha  = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)
sN = Slider(axN, 'Valeur max de n', NMin, NMax, valinit=N0)
salpha = Slider(axalpha, 'alpha', alphamin,alphamax, valinit=alpha0)

    
def update(val):
    N = sN.val
    alpha = salpha.val
    X=signs[:N]*U[:N]**(-1/alpha)
    S=np.cumsum(X)/t[:N]
    l.set_xdata(t[:N]/N)
    l.set_ydata(S)
    fig.canvas.draw_idle()

#plt.legend(loc='best')
sN.on_changed(update)
salpha.on_changed(update)

plt.show()