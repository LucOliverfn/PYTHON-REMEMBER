pessoa = {'nome': 'Lucas', 'sexo': 'masculino', 'idade':22}
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos e é do sexo {pessoa["sexo"]}')
del pessoa['sexo']
pessoa['nome'] = 'soraya'
print (pessoa.keys())
print (pessoa.values())
print (pessoa.items())
for k in pessoa.keys():
    print(k)
for k,v in pessoa.items():
    print (f'{k} {v}')