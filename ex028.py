from random import randint
from time import sleep

pc = randint(0,5)

n = int(input("Digite um número entre 0 e 6: "))
print('Processando...')
sleep(3)

if pc == n:
    print('Parabéns você acerto o número, o número era {}'.format(pc))
else:
    print('Você errou o número, o PC escolheu o número {}!'.format(pc))
