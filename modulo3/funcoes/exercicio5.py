def dobra(lista):
    pos = 0
    while pos<len(lista):
        lista[pos]*=2
        pos+=1
    return(lista)

val =[1,2,3,4,5,6]
dobro = dobra(val)
print (dobro)