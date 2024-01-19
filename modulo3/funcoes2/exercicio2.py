def notas(*n,sit=False):
    '''''
    ->Função para analisar notas e siituação de varios alunos 
    :param n: uma ou mais notas dos alunos (aceita varias)
    :param sit: Valor opcional,indica se deve ou não incluir a situação
    :return: Dicionario com varias informaçãoes sobre a situação da turma
    '''''
    aluno={}
    maior =0
    menor =0
    media =0
    aluno['total'] = len(n)
    for contador in n:
        media += contador
        if menor ==0:
            menor = contador
        else:
            if menor >contador:
                menor = contador


        if maior ==0:
            maior = contador
        else:
            if maior<contador:
                maior = contador
    aluno['menor'] = menor
    aluno['maior'] = maior
    aluno['media'] = media/len(n)
    if sit==True:
        if aluno['media']<6:
            aluno['situacao'] = "Ruim"
        if aluno['media']>=6 and aluno['media']<7.5:
            aluno['situacao'] = "Razoavel"
        if aluno['media']>=7.5:
            aluno['situacao'] = "Boa"
    return(aluno)

resp = notas(5.5,9.5,10,6.5)
print(resp)

#     aluno={}
#     maior =0
#     menor =0
#     media =0
#     aluno['total'] = len(n)
#     aluno['menor'] = min(n)
#     aluno['maior'] = max(n)
    
#     for contador in n:
#         media += contador
        
#     aluno['media'] = media/len(n)
#     if sit==True:
#         if aluno['media']<6:
#             aluno['situacao'] = "Ruim"
#         if aluno['media']>=6 and aluno['media']<7.5:
#             aluno['situacao'] = "Razoavel"
#         if aluno['media']>=7.5:
#             aluno['situacao'] = "Boa"
#     return(aluno)

# resp = notas(5.5,9.5,10,6.5,sit=True)
# # print(resp)