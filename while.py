N = 0
x = input("Entrez un nombre positif : ")
while x > 0:
    x//=2
    N+=1
print("Approx. de log_2 du nombre : "+str(N-1))