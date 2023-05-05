x=range(5)
#Creation et ecriture:
mon_flux=open("my_data.txt","w") #w=write
mon_flux.write(str(x))
mon_flux.close()

#Ecriture a la fin d'un fichier existant:
mon_flux=open("my_data.txt","a") #a=append
mon_flux.write("\n"+str(x+1))
mon_flux.close()

#Lecture:
mon_flux=open("my_data.txt","r") #r=read
y=mon_flux.read()
print(y)