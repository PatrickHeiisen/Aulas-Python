carro = float(input("Qual a velocidade do carro? "))
if carro >= 80:
    multa = (carro - 80) * 7
    print("Multado voce excedeu o limite de 80km")
    print("Voce deve pagar uma multa de R${}".format(multa))
else:
    print("Parabens voce esta abaixo da velocidade..")
