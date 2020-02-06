cidade = input('Digite o nome de uma cidade: ').strip()

check = cidade[:5].upper() == 'SANTO'

if check == True:
    print('Possui')
else:
    print('Não possui')