peso = float(input("Qual e seu peso: "))
altura = float(input("Qual e sua altura: "))

imc = peso / (altura * altura)
print("O IMC desta pessoa e {:.2f}".format(imc))

if imc < 18.5:
    print("Voce esta Abaixo do Peso")
elif imc < 25:
    print("Seu Peso e Ideal")
elif imc < 30:
    print("Voce esta em Sobrepeso")
elif imc < 40:
    print("Voce esta em Obesidade")
else:
    print("Preocupante voce esta em Obesidade Morbida")