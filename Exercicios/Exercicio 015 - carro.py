carro = float(input('Quantos KM rodados: '))
dias = int(input('Quantos dias o carro ficou alugado: '))

alugado = dias * 60
rodado = carro * 0.15
soma = rodado + alugado
print('Total a pagar e de R${:.2f}'.format(soma))

