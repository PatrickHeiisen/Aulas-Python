'''n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}'.format(n, d))
print('O triplo de {} vale {}'.format(n, t))
print('A raiz quadrada de {} e igual a {}'.format(n, r))'''


n = int(input('Digite um numero: '))
print('O dobro de {} vale {}'.format(n, (n * 2)))
print('O triplo de {} vale {}'.format(n, (n * 3)))
print('A raiz quadrada de {} e igual a {:.2f}'.format(n, (n ** (1/2))))

