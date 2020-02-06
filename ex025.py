nome = input('Digite o nome: ')

check = nome.lower().find('silva')

if check == 0:
    print('Possui')
else:
    print('Não possui')