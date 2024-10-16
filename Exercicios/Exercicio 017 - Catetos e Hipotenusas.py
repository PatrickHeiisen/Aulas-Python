import math

'''oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
soma = oposto ** 2 + adjacente ** 2
print('A hipotenusa vai medir {:.2f}'.format(math.sqrt(soma)))'''

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
soma = math.hypot(oposto, adjacente)
print('A hipotenusa vai medir {:.2f}'.format(soma))