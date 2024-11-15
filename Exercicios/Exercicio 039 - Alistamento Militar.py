from datetime import date
atual = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade = atual - nasc
print("Quem nasceu em {} tem {} anos em {}.".format(nasc, idade, atual))
if idade == 18:
    print("Voce precisa se alistar imediatamente")
elif idade < 18:
    soma = 18 - idade
    print("Voce ainda não tem 18 anos, Ainda faltam {} anos para o alistamento".format(soma))
elif idade > 18:
    soma = idade - 18
    print("Voce ja deveria  ter se alistado ha {} anos".format(soma))