nome = input('Digite o nome completo: ')

maius = nome.upper()
minus = nome.lower()
noSpace = nome.split()
aux1 = nome.replace(' ','')
qtde = len(aux1)
qtde1 = len(noSpace[0])

print('A string {} toda maiúscula fica {}'.format(nome,maius))
print('A string {} toda minúscula fica {}'.format(nome,minus))
print('A string {} tem {} letras'.format(nome,qtde))
print('A primeira palavra da string {} tem {} letras'.format(nome,qtde1))
