def area(largura,comprimento):
    
    print (f'A area de um terreno {largura}X{comprimento} é de {largura*comprimento}M²')

def chamada():
    print('    Controle de Terrenos   ')
    print("-"*25)
    lar_T=float(input("LARGURA (M) :"))
    comp_T=float(input("COMPRIMENTO (M) :"))
    area(lar_T,comp_T)

chamada()