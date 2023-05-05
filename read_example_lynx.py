import numpy as np
import matplotlib.pyplot as plt
plt.close("all")
f=open("PopLynxRegionCanada_1821_1934.dat","r")
ytxt=f.readlines() # list de str
y=[int(row) for row in ytxt] # convertit str en int
plt.plot(range(1821,1935),y,"r")
plt.title("Population de lynx")
plt.tight_layout() #pratique pour l'export
plt.show()
