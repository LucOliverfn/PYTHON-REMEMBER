estado = dict()
brasil = list()

for c in range (0,3):
    estado['uf'] = str(input("Digite o Nome do estado :"))
    estado['sigla'] = str(input("Digite o sigla do estado :"))
    print("-"*20)
    brasil.append(estado.copy())
print(brasil)
for contador in brasil:
    for k,v in contador.items():
        print (f'{k} {v}')