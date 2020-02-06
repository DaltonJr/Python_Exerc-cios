n = int(input('Digite a distância da viagem: '))

if n <= 200:
    res = n * 0.5
else:
    res = n * 0.45
print('O valor da passagem é {}'.format(res))

# res = n * 0.50 if n <= 200 else n * 0.45

