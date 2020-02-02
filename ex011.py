lar = float(input('digite a largura da parede a ser pintada: '))
alt = float(input('digite a altura da parede a ser pintada: '))

at = lar * alt
tinta = at / 2

print('para pintar uma parede de {}m², será necessário {} litros de tinta'.format(at,tinta))