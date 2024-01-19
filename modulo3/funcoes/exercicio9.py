from time import sleep
def contagem(inicio,fim,passo):
    if passo<0:
        passo*=-1
    if passo==0:
        passo==1

    if fim>inicio:
        for contador in range(inicio,fim,passo):
            print(f'{contador}', end=' ',flush=True)
            sleep(0.5)
        print(fim)

    else:
        contador = fim
        for contador in range(fim,inicio,passo):
            print(f'{contador}', end='',flush=True)
            sleep(0.5)
        print(inicio)

contagem(9,2,1)
