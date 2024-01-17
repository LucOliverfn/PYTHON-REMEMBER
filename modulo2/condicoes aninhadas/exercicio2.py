import math
numero = int(input("Digite um numero :"))
while True:
    print ("1- Binario\n2- Octal\n3- Hexadecimal\n4- REDEFINIR NUMERO\n5- sair")
    opcao = int(input("escolha uma opção :"))
    if opcao == 1:
        print ("{} convertido para Binario é {}".format(numero,bin(numero)))
    if opcao == 2:
        print ("{} convertido para Octal é {}".format(numero,oct(numero)))
    if opcao == 3:
        print ("{} convertido para Hexadecimal é {}".format(numero,hex(numero)))
    if opcao == 4:
        numero = int(input("Digite um numero :"))
    if opcao == 5:
        break
    else:
        print ("Opção invalida digite novamente")