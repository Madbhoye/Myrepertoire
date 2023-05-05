import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
from matplotlib.widgets import Slider
plt.close("all")


NMin,NMax=1e1,1e5
X = np.random.randn(NMax)
M=max(np.abs(X))
x = np.linspace(-M,M,1000) #vecteur allant de -M a M en 1000 increments
f_x = sps.norm.pdf(x) #densite de la gaussienne

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
N0 = 1e3
alpha0=1./3
plt.plot(x,f_x,"r",linewidth=1.0,label="Gaussian density")
plt.title("Histogram N^alpha columns vs density")
hist, bin_edges = np.histogram(X[:N0], density=True,bins=round(.5*M*N0**alpha0),range=(-M,M))
hist=np.insert(hist,0,0)
hist=np.insert(hist,len(hist),0)
bin_edges=np.insert(bin_edges,len(bin_edges),bin_edges[-1])
l2,=plt.step(bin_edges,hist,"b",label="Histogram")
plt.legend(loc=1)
plt.axis([-M, M, 0, 2*max(f_x)])


axcolor = 'lightgoldenrodyellow'
axN = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)
axalpha  = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)

sN = Slider(axN, "Sample size:", NMin, NMax, valinit=N0)
salpha = Slider(axalpha, 'alpha:', 0., 1., valinit=alpha0)

    
def update(val):
    N = sN.val
    alpha = salpha.val
    hist, bin_edges = np.histogram(X[:N], density=True,bins=round(.5*M*N**alpha),range=(-M,M))
    hist=np.insert(hist,0,0)
    hist=np.insert(hist,len(hist),0)
    bin_edges=np.insert(bin_edges,len(bin_edges),bin_edges[-1])
    l2.set_xdata(bin_edges)
    l2.set_ydata(hist)
    fig.canvas.draw_idle()

#plt.legend(loc='best')
sN.on_changed(update)
salpha.on_changed(update)

plt.show()