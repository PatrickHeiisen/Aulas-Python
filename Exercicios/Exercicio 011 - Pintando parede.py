l = float(input('Largura da parede: '))
a =float(input('Altura da parede: '))

area = l * a
tinta = area / 2

print('Sua parede tem a dimensao de {}x{} e sua area e de {}m²'.format(l, a, area))
print('Para pinta essa parede voce precisara de {}L de tinta'.format(tinta))
