valor1 = int(input('Primeiro Valor: '))
valor2 = int(input('Segundo Valor: '))
valor3 = int(input('Terceiro Valor: '))

# verificando quem e o menor
menor = valor1
if valor2 < valor1 and valor2 < valor3:
    menor = valor2
if valor3 < valor1 and valor3 < valor2:
    menor = valor3
'''if valor3 < valor1 and valor3 < valor2:
   menor = valor3'''
print('O menor valor {}'.format(menor))

# verificando quem e o maior
maior = valor1
if valor2 > valor1 and valor2 > valor3:
    maior = valor2
if valor3 > valor1 and valor3 > valor2:
    maior = valor3
'''if valor3 > valor1 and valor3 > valor2:
    maior = valor3'''
print('O maior valor {}'.format(maior))

