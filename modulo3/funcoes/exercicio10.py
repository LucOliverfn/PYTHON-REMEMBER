import random
import time
def sorteio():
        numeros = []
        print ('Sorteando 5 valores da lista',end=': ')
        for contador in range (0,5,1):
                numero = random.randint(1,10)
                print(f'{numero}',end=' ',flush=True)
                time.sleep(0.5)
                numeros.append(numero)
        print("PRONTO!")
        soma_par(numeros)

def soma_par(lista):
        soma = 0
        for numero in lista:
                if (numero%2==0):
                        soma += numero
        print(f'Somando os valores pares de {lista}, temos {soma}')

sorteio()