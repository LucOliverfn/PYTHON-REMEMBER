notas = []
temp = []
while True:
    temp.append(str(input("Nome :")))
    temp.append(float(input("Nota 1 :")))
    temp.append(float(input("Nota 2 :")))
    notas.append(temp[:])
    temp.clear()
    decisao = str(input("DESEJA CONTINUAR? (S/N) :"))
    if decisao in 'Nn':
        break
print ("-="*20)
print ("No.  Nome             Media")
print ("-"*40)
for indice, lista in enumerate(notas):
    print (f'{indice}    {notas[indice][0]}               {(notas[indice][1]+notas[indice][2])/2}')
print ("-"*40)
while True:
    escolha = int(input("Deseja ver a nota de qual aluno (999 interrompe) :"))

    if escolha ==999:
        break
    else:
        print(f'As notas de {notas[escolha][0]} são {notas[escolha][1]} e {notas[escolha][2]}')