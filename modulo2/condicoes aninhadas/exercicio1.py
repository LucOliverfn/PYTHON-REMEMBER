casa = float(input("Qual o valor da casa que voce deseja comprar? :"))
salario = float(input("Qual o valor do seu salario? :"))
anos = int(input("quantos anos voce quer pagar a casa? :"))

parcela = casa/(anos*12)

if parcela<=salario*(30/100):
    print ("As parcelas da casa de valor {:.2f} em {} anos vao ser de {:.2f} reais.".format(casa,anos,parcela))
else:
    print ("Emprestimo negado")