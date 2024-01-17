print ("MOstra pares")
print ("informe o intervalo que voce deseja mostrar os pares")
n1 = int(input("A contagem vai começar no numero :"))
n2 = int(input("A contagem vai acabar no numero :"))
for contador in range (n1,n2,1):
    if (contador%2==0):
        print (contador)
if (n2%2==0):
    print (n2)