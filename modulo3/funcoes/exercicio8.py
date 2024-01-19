def escreva(par):
    print ('~'*(len(par)+4))
    print(f'  {par}')
    print ('~'*(len(par)+4))

def chamada():
    txt = str(input('Digite o texto  :'))
    escreva(txt)

chamada()