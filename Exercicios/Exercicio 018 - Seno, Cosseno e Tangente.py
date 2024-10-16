import math
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo de {} tem o Seno de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o Cosseno de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem a Tangente de {:.2f}'.format(angulo, tangente))