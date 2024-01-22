def leiaDinheiro():
    money = str(input("Digite um Valor :"))
    if money.isnumeric():
        return(money)
    else:
        print("ERRO DIGITE UM NUMERO VALIDO")
        
def menu():
    print("--"*20)
    print(      'Resumo do valor        ')
    print("--"*20)

def dados(preco):
    from funcoes.mat.dado import dobro,aumentar,reduzir,metade
    preco = float(preco)
    print(f'Preço analisado: R${preco}')
    print(f'Dobro do preço: R${dobro(preco)}')
    print(f'Matade do preço: R${metade(preco)}')
    print(f'aumento em 10% do preço: R${aumentar(preco)}')
    print(f'redução em 13% do preço: R${reduzir(preco)}')