from datetime import date

nasc = int(input('Digite o ano de nascimento: \n'))

ano = date.today().year

res = ano - nasc

if res < 18:
    res2 = 18 - res
    print('com {} anos, ainda vai se alistar, faltam {} anos para se alistar'.format(res, res2))
elif res == 18:
    print('com {} anos, deve se alistar esse ano'.format(res))
elif res > 18:
    res2 = res - 18
    print('com {} anos, o tempo de alistamento já passou fazem {} anos'.format(res, res2))


