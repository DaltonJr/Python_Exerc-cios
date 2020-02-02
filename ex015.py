km = float(input('qual a distância em km que o carro percorreu? '))
dias = float(input('por quantos dias o carro foi alugado? '))

tkm = km * 0.15
tdia = dias * 60

total = tkm + tdia

print('Percorrendo {}kms, durante {} dias o preço total a pagar é de R${:.2f}'.format(km,dias,total))

