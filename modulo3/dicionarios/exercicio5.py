import random
from time import sleep
jogo = []
pessoa ={}
ranking = {}
print ("Valores sorteados:")
for contador in range (0,5):
    pessoa['nome'] = (f'jogador{contador+1}')
    pessoa['dado'] = random.randint(1,6)
    jogo.append(pessoa.copy())
for contador in range (0,5):
    sleep(0.5)
    print(f'O {jogo[contador]["nome"]} tirou {jogo[contador]["dado"]}')
