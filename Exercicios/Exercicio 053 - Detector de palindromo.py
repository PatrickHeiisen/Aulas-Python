frase = str(input("Digite uma frase: ")).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1,-1):
    inverso += junto[letra] 
if inverso == junto:
    print("Temos um Palindromo")
else:
    print("A frase digitada nao e um Palindromo")





print("Voce digitou a frase {}".format(frase))
