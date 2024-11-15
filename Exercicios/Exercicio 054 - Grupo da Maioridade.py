from datetime import date
atual =date.today().year
totalmaior = 0
totalmenor = 0
for pes in range(1,5):
    nasc = int(input("Em que ano a pessoa a {}° pessoa nasceu: ".format(pes)))
    idade = atual - nasc
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1 
print("Ao todo tivemos {} pessoas maiores de idade.".format(totalmaior))
print("E tambem tivemos {} pessoas menores de idade.".format(totalmenor))