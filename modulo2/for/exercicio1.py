from time import sleep
print("Contagem regresiva")

comeco = int(input("Digite qual o inicio da contagem :"))
final = int(input("Digite qual o fim da contagem :"))
passo = int(input("Digite qual passo da contagem :"))

for c in range (comeco,final,-passo):
    print (c)
    sleep(0.5)