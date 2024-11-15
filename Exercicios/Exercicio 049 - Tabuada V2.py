# 1 Jeito
'''tabuada = int(input("Digite um numero para ver sua tabuada: "))
for n in range(1, 11):
    soma = tabuada * n
    print('{} x {} = {}'.format(tabuada, n, soma))'''
    
# 2 Jeito
tabuada = int(input("Digite um numero para ver sua tabuada: "))
for n in range(1,11):
    print('{} x {} = {}'.format(tabuada, n, tabuada*n))
