km = int(input('Qual a distancia da viagem: '))
if km <= 200:
    soma = km * 0.50
    print('Sua viagem vai custar R$ {}'.format(soma))
else:
    soma = km * 0.45
    print('Sua viagem vai custar R$ {}'.format(soma))