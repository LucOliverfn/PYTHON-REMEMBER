from time import sleep
classe=[]
aluno ={}
while True:
    aluno['nome'] =str(input("Digite o nome do Aluno :"))
    aluno ['media'] = float(input(f'Digite a media de {aluno["nome"]} :'))
    classe.append(aluno.copy())
    decisao=str(input("Deseja continuar? (S/N):"))
    if decisao in 'nN':
        break
while True:
    for contador in range (0,len(classe)):
        print (f'{contador} ----> {classe[contador]["nome"]}')
    sleep(0.20)
    escolha=int(input("Qual aluno vc quer ver as notas? (999 interrompe) :"))
    if (escolha ==999):
        break
    else:
        print(f'Aluno {classe[escolha]["nome"]} possui a nota {classe[escolha]["media"]}')
        sleep(0.20)
        if (classe[escolha]["media"]>=6.0):
            print ("A situação do aluno é APROVADO")
        else:
            print ("A situação do aluno é REPROVADO")


