velocidade = int(input("Digite a velocidade do carro (KM/H): "))
if velocidade<=80:
    print ("Esta dentro do limite de velocidade, Parabêns")
else:
    multa = (velocidade-80)*7
    print ("Você recebeu uma multa no valor de R${},00 por estar a {} Km/h em uma pista que o limite é 80".format(multa,velocidade))