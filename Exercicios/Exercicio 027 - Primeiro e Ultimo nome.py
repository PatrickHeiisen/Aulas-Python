n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito Prazer em te Conhecer!!!')
print('Seu Primeiro nome é {}'.format(nome[0]))
print('Seu Ultimo nome é {}'.format(nome[len(nome)-1]))

