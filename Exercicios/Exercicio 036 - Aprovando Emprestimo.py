casa = int(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$'))
financiamento = int(input('Quantos anos de financiamento? '))

prestacao = casa  / (financiamento * 12)
minimo = salario * 30 / 100

if prestacao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO')
    
print('Para pagar uma casa de R$ {} em {} anos a prestação sera de R$ {:.2F}'.format(casa, financiamento, prestacao))
