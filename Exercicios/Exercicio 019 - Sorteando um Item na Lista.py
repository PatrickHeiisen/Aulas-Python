import random
pri = str(input('Primeiro Aluno: '))
seg = str(input('Segundo Aluno: '))
ter = str(input('Terceiro Aluno: '))
qua = str(input('Quarto Aluno: '))

lista = [pri, seg, ter, qua]
aluno = random.choice(lista)
print('O aluno escolhido foi {}'.format(aluno))