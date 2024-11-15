produto = float(input('Valor do produto R$ '))

parcelado = produto + (produto * 10 / 100)
desconto = produto - (produto * 15 / 100)

print('Valor a vista tem 15% de desconto, preco final R${:.2f}'.format(desconto))
print('Valor parcelado tem aumento de 10%, preco final R${:.2f}'.format(parcelado))

