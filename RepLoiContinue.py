import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

n = int(1e5) #taille de l'echantillon
X = np.random.randn(n) #echantillon
MinX, MaxX=min(X), max(X)
N=round(n**(1./3.)*(MaxX-MinX)/3.49) #nombre de colonnes

plt.figure(1) 
x = np.linspace(MinX,MaxX,1000)
f_x = sps.norm.pdf(x) #Densite gaussienne
plt.plot(x,f_x,"r",linewidth=1.0,label="Densite gaussienne")
#Affichage histo:
plt.hist(X, bins=N, normed=True,histtype='step',label="Histogramme")
plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.05),ncol=2,fancybox=1,shadow=1)
plt.title("Histogramme vs densite theorique")
plt.show()

plt.figure(2) 
X.sort()
F_x = sps.norm.cdf(x)
plt.plot(x,F_x,"r",linewidth=1.0,label="Fct de rep gaussienne")
#Affichage fct rep empirique
F_x_n = np.arange(1,n+1,dtype=np.double)/n
plt.plot(X,F_x_n,"b",label="Fct de rep empirique")
plt.legend(loc='upper center',bbox_to_anchor=(0.5, -0.05),ncol=2,fancybox=1,shadow=1)
plt.title("Fct de rep empirique vs theorique")
plt.show()