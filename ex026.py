frase = input('digite uma frase: ').lower().strip()

cont = frase.count('a')
first = frase.find('a')
last = frase.rfind('a')



print('A letra a aparece {} vez(es)'.format(cont))
print('A primeira vez que a letra "a" aparece é na posição {}'.format(first + 1))
print('a última vez que a letra "a" aparece é na posição {}'.format(last + 1))   