numeros=[]
mai =0
indi_mai = []
men=0
indi_men = []
for c in range(0,5,1):
    n = int(input("Digite o {}° valor :".format(c+1)))
    numeros.append(n)
    if c==0:
        mai = men = numeros[c]
    else:
        if numeros[c]>mai:
            mai=numeros[c]
        if numeros[c]<men:
            men=numeros[c]
for indice,valor in enumerate(numeros):
    if valor==mai:
        indi_mai.append(indice)
    if valor==men:
        indi_men.append(indice)


print (f'você Digitou os valore{numeros}')
print (f'O maior numero digitado foi {mai} nas posições {indi_mai}')
print(f'O menor numero digitado foi {men} nas posiçoes {indi_men}')