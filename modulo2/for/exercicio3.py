print ("soma impares")
print ("informe o intervalo que voce deseja somar os impares")
n1 = int(input("A contagem vai começar no numero :"))
n2 = int(input("A contagem vai acabar no numero :"))
soma = 0
for contador in range (n1,n2,1):
    if (contador%2==1) and (contador%3==0):
        soma = soma+contador
print (soma)