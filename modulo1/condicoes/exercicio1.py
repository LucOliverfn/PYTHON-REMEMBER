import random
comp = random.randint(0,5)
num = int(input("DIgite o numro para adivinhar o que o computador pensou de 0 a 5: "))
if num==comp:
    print ("Parabens você acertou o computador pensou no numero {}".format(comp))
else:
    print("Você errou, o computador escolheu o numero {}".format(comp))
