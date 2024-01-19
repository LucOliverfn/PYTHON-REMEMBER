def leiaint(titulo):

    while True:
        numero = str(input(titulo))
        if numero.isnumeric():
            return(numero)
        else:
            print (f'ERRO! Digite um numero inteiro válido.')
            
    
n1 = leiaint('Digite um numero: ')
print(f'Você digitou o numero inteiro {n1}')

