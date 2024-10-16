p = float(input('Qual e preço do produto? R$ '))

desc = p * 0.05
pdesc = p - desc

print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(p, pdesc))