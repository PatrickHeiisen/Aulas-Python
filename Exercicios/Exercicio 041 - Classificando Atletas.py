ano = int(input("Digite seu ano de nascimento: "))
atual = 2024
idade = atual - ano

print("A pessoa que nasceu em {} tem {} anos e esta na categoria...".format(ano, idade))

if idade <= 9:
    print("Classificação MIRIM")
elif idade <= 14:
    print("Classificação INFANTIL")
elif idade <= 19:
    print("Classificação JUNIOR")
elif idade <= 25:
    print("Classificação SENIOR")
else:
    print("Classificação MASTER")
    