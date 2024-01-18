numeros = []
indice = []
while True:
    num = int(input("Digite um numero :"))
    numeros.append(num)
    deci=str(input("Deseja continuar ? (S/N) :"))
    if deci=="N":
        numeros.sort(reverse=True)
        break
print(f'Foram digitados {len(numeros)} numeros')
print(f'A lista em ordem decrescente é {numeros}')
if 5 in numeros:
    print ("O numero 5 está presente na lista")
else:
    print ("O numero 5 NÃO está presente na lista")