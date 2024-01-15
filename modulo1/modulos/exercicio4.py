import random
cont = 0
lista = []
for cont in range (0,4,1):
    num = str(input("digite um nome :"))
    lista.append(num)
random.shuffle (lista)

for cont in range (0,4,1):
    print ("{}-{}".format(cont+1,lista[cont]))