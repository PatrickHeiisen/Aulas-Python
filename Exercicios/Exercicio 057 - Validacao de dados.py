sexo = str(input("Informe seu sexo [M/F]")).upper().strip()
while sexo not in 'MmFf':
    sexo = str(input('Dados Invalidos. Por favor, Informe seu sexo: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))


