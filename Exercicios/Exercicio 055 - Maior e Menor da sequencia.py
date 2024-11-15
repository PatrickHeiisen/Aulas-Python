maior = 0
menor = 0
for p in range(1,5):
    peso = float(input("Peso da {} pessoa".format))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = Peso
print("O maior peso lido foi de {}Kg".format(maior))
print("O menor peso lido foi de {}Kg".format(menor))
