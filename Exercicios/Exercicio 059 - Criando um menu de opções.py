pri = int(input("Primeiro valor: "))
seg = int(input("Segundo valor: "))
opcao = 0
while opcao != 5:
    opcao = int(input(''' 
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    >>>>> Qual sua opção: '''))
    
    if opcao == 1:
        soma = pri + seg
        print("A soma entre {} e {} igual a {}".format(pri, seg, soma))
    elif opcao == 2:
        soma = pri * seg
        print("A multiplicação entre {} e {} igual a {}".format(pri, seg, soma))
    elif opcao == 3:
        if pri > seg:
            print("Entre {} e {} o numero maior e {}".format(pri, seg, pri))
        else:
            print("Entre {} e {} o numero maior e {}".format(pri, seg, seg))
    elif opcao == 4:
        print("Informe os numeros novamente!!!")
        pri = int(input("Primeiro valor: "))
        seg = int(input("Segundo valor: "))
    elif opcao == 5:
        print("Fim do programa! Volte sempre!!!")
    else:
        print("Opção Invalida...Tente Novamente")
    print("=-=" * 13)
    