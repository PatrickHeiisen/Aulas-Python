'''for  c in range(1,6):
    print('Oi')
print('Fim')'''

'''for c in range(6,0, -1): #Conta de tras pra frente
    print(c)
print('Fim')'''

'''n = int(input('Digite um numero: '))
for c in range (0, n+1):
    print(c)
print('Fim')'''

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('Fim')

s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatorio de todos os valores foi {}'.format(s))