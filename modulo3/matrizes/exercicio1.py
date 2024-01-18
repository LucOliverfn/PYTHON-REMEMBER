pessoas = []
guy = []

mai = men = 0
while True:
    guy.append(str(input("Digite o nome :")))
    guy.append(float(input(f'Digite o peso  :')))
    pessoas.append(guy[:])

    if len(pessoas)==0:
        mai = men = guy[1]
    else:
        if guy[1] > mai:
            mai = guy[1]
        if guy[1] < men:
            men = guy[1]    
    
    escolha=(str(input("Deseja continuar? (S/N) :")))
    guy.clear()
    if escolha in 'nN':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O menor peso registrado foi de {men}kg. Peso de ',end='')
for p in pessoas:
    if p[1] ==men:
        print(f'{p[0]}',end='')  
print()
print(f'O maior peso registrado foi de {mai}kg. Peso de ',end='')
for p in pessoas:
    if p[1] ==mai:
        print(f'{p[0]}',end='')  
print()
