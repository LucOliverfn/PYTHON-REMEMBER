pessoa = {}

while True:
    pessoa['nome'] = str(input("Digite o nome :"))
    ano = int(input("Digite o ano de Nascimento :"))
    pessoa['idade'] = 2023-ano
    pessoa['CTPS'] = int(input("Digite a Carteira de trabalho (0 se não tem): "))
    if pessoa['CTPS']==0:
        break
    else:
        pessoa['contratacao'] = int(input("Digite o ano de contratrção :"))
        pessoa['salario'] = float(input("Digite o Salario :"))
        pessoa['aposentadoria'] = (pessoa['contratacao']-ano)+35
        break
print(pessoa)
for k,v in pessoa.items():
    print(f'{k} tem o valor de {v}')