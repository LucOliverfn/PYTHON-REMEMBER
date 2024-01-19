def soma(*val):
    soma=0
    for contador in val:
        soma+=contador
    print(f'Somando os valores {val} temos {soma}')


soma(2,3,4,5)
soma(4,5)
soma(1)