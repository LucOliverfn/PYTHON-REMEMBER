def contador(*num):
    tam = len(num)
    for valor in num:
        print(f' {valor} ',end=' ')
    print('FIM')
    print(f'foram inseridos {tam} numeros')

contador(2,3,4,5,6)
contador(1,2,3)
contador(1)