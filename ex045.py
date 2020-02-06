from random import randint

pc = randint(0,2)

user = int(input('Digite o número referente a sua escolha para o jogo \n [ 1 ] - Pedra \n [ 2 ] - Papel \n [ 3 ] - Tesoura \n'))

#pedra
if user == 1:   
    if pc == 0:
        print('empate')
    elif pc == 1:
        print('PC ganhou')
    elif pc == 2:
        print('Você ganhou')

#papel
if user == 2:
    if pc == 0:
        print('Você ganhou')
    elif pc == 1:
        print('Empate')
    elif pc == 3:
        print('PC ganhou')

#tesoura
if user == 3:
    if pc == 0:
        print('PC ganhou')
    elif pc == 1:
        print('Você ganhou')
    elif pc == 2:
        print('empate')

print('Você escolheu:')
if user == 1:
    print('Pedra')
elif user == 2:
    print('Papel')
elif user == 3:
    print('Tesoura')

print('O computador escolheu:')
if pc == 0:
    print('Pedra')
elif pc == 1:
    print('Papel')
elif pc == 2:
    print('Tesoura')
