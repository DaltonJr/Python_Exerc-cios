n1 = int(input('Digite um número: \n'))
n2 = int(input('Digite um número: \n'))
n3 = int(input('Digite um número: \n'))

maior = n1

if (n2 > maior):
    maior = n2
if (n3 > maior):
    maior = n3

print('Maior: ',maior)

menor = n1

if (n2 < menor):
    menor = n2
if (n3 < menor):
    menor = n3

print('Menor: ',menor)


print('o número maior é {}, e o número menor é {}.'.format(maior,menor))
2