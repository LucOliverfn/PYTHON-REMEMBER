import random
from time import sleep
jogos = []
jogo = []
tot=1
escolha = int(input("Digite a Quantidade de jogos que voce quer :"))
while tot <=escolha:
    while True:
        num = random.randint(1,60)
        if num not in jogo:
            jogo.append(num)
        if len(jogo)==6:
            break
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    tot+=1
for indice, lista in enumerate(jogos):
    print(f'Jogo {indice+1}: {lista}')
    sleep(1)
print("BOA SORTE")