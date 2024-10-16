real = float(input('Quanto de dinheiro voce tem na carteira? R$ '))
dolar = real / 5.4715
euro = real / 6.0338
print('Com R${:.2f} voce pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} voce pode comprar EU${:.2f}'.format(real, euro))
