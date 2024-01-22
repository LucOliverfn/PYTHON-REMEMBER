from moeda.operacoes import metade,dobro,aumentar,reduzir
p = float(input("Digite o preço : R$"))
print (f'A metade de R${p} é R${metade(p)}')
print (f'O dobro de R${p} é R${dobro(p)}')
print (f'Aumentando 10% de R${p}, temos R${aumentar(p)}')
print (f'Reduzindo 13% de R${p}, temos R${reduzir(p)}')