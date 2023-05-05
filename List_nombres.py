nombres = [17, 38, 10, 25, 72]
nombres.sort()
nombres # [10, 17, 25, 38, 72]
nombres.append(12)
nombres # [10, 17, 25, 38, 72, 12]
nombres.reverse()
nombres # [12, 72, 38, 25, 17, 10]
nombres.remove(38)
nombres # [12, 72, 25, 17, 10]
nombres.index(17) # 3
nombres[0] = 11
nombres[1:3] = [14, 17, 2]
nombres # [11, 14, 17, 2, 17, 10]
nombres.count(17) # 2
mean(nombres) # moyenne
std(nombres) # ecart-type