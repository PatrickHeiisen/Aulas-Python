nome = str(input('Digite uma Frase : ')).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(nome.count('A')))
print('A primeira letra A aparece na posição {}.'.format(nome.find('A')+1))
print('A ultima letra A aparece na posição {}.'.format(nome.rfind('A')+1))
