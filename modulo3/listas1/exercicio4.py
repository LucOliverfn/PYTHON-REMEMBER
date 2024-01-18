par = []
impar = []
numeros = []
while True:
    num = int(input("Digite um numero :"))
    numeros.append(num)
    if num%2==0:
        par.append(num)
    else:
        impar.append(num)
    deci=str(input("Deseja continuar ? (S/N) :"))
    if deci=="N":
        break
print (f'Os numeros digitados foram {numeros}')
print (f'Os numeros impares digitados foram {impar}')
print (f'Os numeros pares digitados foram {par}')
