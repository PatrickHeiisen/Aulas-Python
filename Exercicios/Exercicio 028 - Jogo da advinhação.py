from random import randint
print("Digite um numero de 0 a 5")
num = int(input("Em que numero eu estou pensando? "))
computador = randint(0, 5)
if num == computador:
    print("Vc Acertou")
else:
    print("Vc Errou")
    

