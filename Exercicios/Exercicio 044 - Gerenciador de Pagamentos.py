preco = float(input("Preço das Compras R$ "))

print("FORMAS DE PAGAMENTO")
print("[1] a vista dinheiro/cheque")
print("[2] a vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")

opcao = int(input("Qual e a opção: "))

if opcao == 1:
    soma = preco - (preco * 10 / 100)
    print("Sua compra custava R${} com desconto de 10% deu R${}".format(preco, soma))
elif opcao == 2:
    soma = preco - (preco * 5 / 100)
    print("Sua compra custava R${} com desconto de 5% deu R${}".format(preco, soma))  
elif opcao == 3:
    print("Você não teve desconto na sua compra, o valor a pagar e de R${}".format(preco)) 
elif opcao == 4:
    soma = preco + (preco * 20 / 100)
    print("Sua compra custava R${} com juros de 20% deu R${}".format(preco, soma))  
else:
    print("Opção Invalida!!!!. Tente Novamente")