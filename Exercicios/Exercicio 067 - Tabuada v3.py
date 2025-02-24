while True:
    tabuada = int(input('Quer ver a tabuada de qual valor?: '))
    print('='*35)
    if tabuada < 0:
        break
    for n in range(1, 11):
        print(f'{tabuada} x {n} = {tabuada * n}')
    print('='*35)
print('Programa TABUADA ENCERRADO. Volte sempre!!!')
