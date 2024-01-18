
numeros = []
while True:
    num = int(input("Digite um numero :"))
    if num in numeros:
        print("Numero Duplicado Não irei adicioar ele.... ")
    else:
        numeros.append(num)
        print("Numero Adicionado com sucesso....")

    deci=str(input("Deseja continuar ? (S/N) :"))
    if deci=="N":
        numeros.sort()
        break
print(f'Os numeros digitados e contidos na lista são {numeros}')