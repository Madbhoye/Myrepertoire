import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

E = np.random.randn(int(1e5))#echantillon

x = np.linspace(-4,4,1000)
f_x = sps.norm.pdf(x) #Densite gaussienne
plt.plot(x,f_x,"r",label="Theory")
#Affichage histo:
plt.hist(E,bins=50,normed=1,\
    histtype='step',label="Data")
plt.legend(loc='best')
plt.show()

 