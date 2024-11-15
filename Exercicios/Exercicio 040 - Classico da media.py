num1 = float(input("Primeira Nota: "))
num2 = float(input("Segunda Nota: "))

nota = (num1 + num2) / 2

if nota >= 7.0:
    print("Aluno Aprovado")
elif nota >= 5 and nota < 7:
    print("Aluno esta de Recuperacao")
else:
    print("Aluno Reprovado")