'''print(5+2)
print(5-2)
print(5*2)
print(5/2)
print(5**2)
print(5//2)
print(5%2)'''

'''print(5+3*2)
print(365**522)'''

'''print(81**(1/2)) #Raiz Quadrada de 81
print('='*20)
print(25**(1/2)) #Raiz Quadrada de 25
print('='*20)
print(127**(1/3)) #Raiz Cubica de 127'''

'''nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))'''

#Quebrar linha \n
#Deixar dois Prints na mesma linha (end='')
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e {}, o produto e {} e a divisão e {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potencia {}'.format(di, e))
