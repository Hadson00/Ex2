contador = 0
vetor = []

while contador < 20:
    x = int(input("Digite um numero: "))
    vetor.append(x)
    contador += 1

contador = 0
while contador < 20:
    if vetor[contador] < 10 and vetor[contador] > 0: 
        x = 1
        print(x)
        contador += 1
    elif vetor[contador] < 0: 
        x = 0
        print(x)
        contador += 1
    else:
        x = 2
        print(x)
        contador += 1