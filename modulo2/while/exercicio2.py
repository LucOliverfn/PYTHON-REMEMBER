import random
from time import sleep
print("Jogo da Adivinhação")
pc = random.randint(0,10)
tentativas = 0
while True:
    numero = int(input("Digite um numero de 0 a 10 :"))
    tentativas = tentativas + 1
    if numero==pc:
        print ("Parabens Voce acertou em {} tentativas, o numero que o compudor pensou foi {}".format(tentativas,pc))
        break
    else:
        print("O numero digitado não é o que o computador pensou tente novamente.")
        sleep (0.5)