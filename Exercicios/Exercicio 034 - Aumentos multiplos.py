salario = float(input('Qual e o salario do funcionario: '))

if salario > 1250:
    soma = (salario * 10 / 100) + salario
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora'.format(salario, soma))
if salario <= 1250:
    soma = (salario * 15 / 100) + salario
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f}} agora'.format(salario, soma))
