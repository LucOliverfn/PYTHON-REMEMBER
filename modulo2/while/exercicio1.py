print("Sabendo o seu sexo")
while True:
    sexo = str(input("Digite o seu sexo (M/F):" ))

    if (sexo=="M"):
        print("Seu sexo é masculino")
        break
    if (sexo=="F"):
        print("Seu sexo é feminino") 
        break
    else:
        print("OPÇÃO INCORRETA,tente novamente.")
