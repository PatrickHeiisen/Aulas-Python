somaidade = 0
mediaidade = 0
maiorhomem = 0
nomevelho = 0
totmulher20 = 0

for p in range(1, 5):
    print("------ {}* PESSOA --------".format(p))
    nome = str(input("Nome: ")).strip
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]")).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in "Mm":
        maiorhomem = idade
        nomevelho = nome
    if sexo in "Mn" and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
        
mediaidade = somaidade / 4
print("A media de idade do grupo e de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maiorhomem, nomevelho))
print("Ao todo são {} mulheres com menos de 20 anos".format(totmulher20))
