import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
from matplotlib.widgets import Slider
plt.close("all")


NMin,NMax,NTCLMin,NTCLMax=1.,1e3,1.,1e4
alphamin,alphamax=.8,4.
signs = 2*np.random.binomial(1,.5,size=(NTCLMax,NMax))-1
U = np.random.rand(NTCLMax,NMax)

#def f(a):
#    return 2+(a-alphamin+.001)**(-5)

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
N,NTCL= NMax/2.,1e3
alpha=2.
X=signs[:NTCL,:N]*U[:NTCL,:N]**(-1/alpha)
S=np.sum(X, axis=1)
S-=np.mean(S)
S/=np.std(S)
M0=4
M=max(np.abs(S))
x = np.linspace(-M0,M0,1000) #vecteur allant de -M a M en 1000 increments
f_x = sps.norm.pdf(x) #densite de la gaussienne
plt.title("Error histogram vs gaussian density")
plt.plot(x,f_x,"r",linewidth=1.0,label="Gaussian density")
hist, bin_edges = np.histogram(S,density=True,bins=round(M*NTCL**(1./3)))#*f(alpha)))#,range=(-M0,M0))
hist=np.insert(hist,0,0)
hist=np.insert(hist,len(hist),0)
bin_edges=np.insert(bin_edges,len(bin_edges),bin_edges[-1])
l2,=plt.step(bin_edges,hist,"b",label="Error histogram")
plt.axis([-M0, M0, 0, 1.5*max(f_x)])
 


axcolor = 'lightgoldenrodyellow'
axNTCL = plt.axes([0.25, 0.05, 0.65, 0.03], axisbg=axcolor)
axN = plt.axes([0.25, 0.15, 0.65, 0.03], axisbg=axcolor)
axalpha  = plt.axes([0.25, 0.1, 0.65, 0.03], axisbg=axcolor)

sNTCL = Slider(axNTCL, "Sample size:", NTCLMin, NTCLMax, valinit=NTCL)
sN = Slider(axN, 'n:', NMin, NMax, valinit=N)
salpha = Slider(axalpha, 'alpha:', alphamin,alphamax, valinit=alpha)

    
def update(val):
    N = sN.val
    NTCL = sNTCL.val
    alpha = salpha.val
    X=signs[:NTCL,:N]*U[:NTCL,:N]**(-1/alpha)
    S=np.sum(X, axis=1)
    S-=np.mean(S)
    S/=np.std(S)
    M=np.max(abs(S))
    hist, bin_edges = np.histogram(S,density=True,bins=round(M*NTCL**(1./3)))#*f(alpha)))#,range=(-M0,M0))
    hist=np.insert(hist,0,0)
    hist=np.insert(hist,len(hist),0)
    bin_edges=np.insert(bin_edges,len(bin_edges),bin_edges[-1])
    l2.set_xdata(bin_edges)
    l2.set_ydata(hist)
    fig.canvas.draw_idle()

sN.on_changed(update)
sNTCL.on_changed(update)
salpha.on_changed(update)

plt.show()