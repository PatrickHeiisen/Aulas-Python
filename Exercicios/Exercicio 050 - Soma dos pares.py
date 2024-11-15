soma = 0
cont = 0
for n in range(1, 7):
    num = int(input('Digite o {} valor: '.format(n)))
    if num % 2 == 0: # para saber se o numero e par
        soma += num
        cont += 1
print('Voce informou {} numeros Pares e a soma foi {}'.format(cont, soma))
