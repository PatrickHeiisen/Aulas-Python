num = int(input("Digite um numero inteiro: "))
print('''Escolha uma das bases para conversão
[1]converter para Binario
[2]converter para Octal
[3]converter para Hexadecimal''')
base = int(input("Sua opção: "))

if base == 1:
    print("{} convertido para Binario e igual a {}".format(num, bin(num)[2:]))
elif base == 2:
    print("{} convertido para Binario e igual a {}".format(num, oct(num)[2:]))
elif base == 3:
    print("{} convertido para Binario e igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção invalida Tente Novamente!!!")