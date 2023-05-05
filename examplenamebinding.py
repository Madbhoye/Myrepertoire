x = [4, 2, 10, 9, "toto"]
y = x  # y: seulement un alias de x,
       # pas de copie effectuee ici
y[2] = "tintin" # change x(2) en "tintin"
print(x) # [4, 2, "tintin", 9, "toto"]
x = [4, 2, 10, 9, "toto"]
y = x[:]   # On demande une copie
y[2] = "tintin" # modifie y mais pas x
print(x) #  [4, 2, 10, 9, "toto"]
print(y) # [4, 2, "tintin", 9, "toto"]