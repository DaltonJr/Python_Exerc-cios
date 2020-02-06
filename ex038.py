n1 = int(input('Digite um número: \n'))
n2 = int(input('Digite um número: \n'))

if n1 > n2:
    print('o primeiro valor {}, é maior.'.format(n1))
elif n2 > n1:
    print('o segundo valor {}, é maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são iguais.')
