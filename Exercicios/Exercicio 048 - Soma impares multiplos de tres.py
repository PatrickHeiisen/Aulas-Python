soma = 0 # Acumulador
cont = 0 # conta os numeros impares
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += c
        soma = soma + c
print('A soma de todos os {} valores solicitados e {}'.format(cont, soma))
