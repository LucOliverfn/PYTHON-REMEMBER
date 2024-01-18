jogador ={}
gols =[]
total =0
jogador['nome'] = str(input("Digite o nome do jogador :"))
jogador['partida'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? :'))

for contador in range(0,jogador['partida']):
    gols.append(int(input(f'Quantos gols na partida {contador+1}? :')))
    total += gols[contador]
jogador['gols'] = gols
jogador['total'] = total
print("-="*25)
print (jogador)
print("-="*25)
for k,v in jogador.items():
    if k!="partida":
        print(f'O campo(chave) {k} tem o valor {v}')
print("-="*25)
print (f'O jogador {jogador["nome"]} jogou {jogador["partida"]} partidas')
for contador in range (0,jogador["partida"]):
    print (f'=> Na partida {contador+1}, fez {jogador["gols"][contador]}')
print(f'Foi um total de {jogador["total"]} gols')
