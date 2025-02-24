resp = 's'
soma = quantidade = media = maior = menor = 0
while resp in 'Ss':
    numero = int(input('Digite um numero: '))
    soma += numero  # Adiciona o número à soma
    quantidade += 1  # Incrementa o contador
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resp = str(input('Quer Continuar[s/n]: ')).upper().strip()
    
media = soma / quantidade
print('Voce digitou {} numeros e a media foi {}'.format(quantidade, media))
print('O maior valor foi {} e o menor {}'.format(maior, menor))

