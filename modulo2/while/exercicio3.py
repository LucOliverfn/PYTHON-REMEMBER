from time import sleep
print ("menuzin brbao da matematica")
n1= (int(input("Digite o primeiro numero :")))
n2= (int(input("Digite o segundo numero :")))
while True:
    print("----------------------------------------")
    print("1- somar\n2-multiplicar\n3-maior\n4-Novos numeros\n5-Sair")
    print("----------------------------------------")
    escolha = int(input("escolha uma opção :"))
    if escolha==1:
        print("a soma de {} e {} é {}".format(n1,n2,n1+n2))
        sleep(0.25)
    elif escolha==2:
        print("a multiplicação entre {} e {} é {}".format(n1,n2,n1*n2))
        sleep(0.25)
    elif escolha==3:
        if n1>=n2:
            print("O maior numero digitado é {}".format(n1))
        else:
            print("O maior numero digitado é {}".format(n2))
    elif escolha==4:
        print ("DIgite os novos numeros")
        sleep(0.25)
        n1= (int(input("Digite o primeiro numero :")))
        n2= (int(input("Digite o segundo numero :")))
        sleep(0.25)
    elif escolha==5:
        break