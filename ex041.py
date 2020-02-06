from datetime import date

nasc = int(input('Digite o ano de nascimento: \n'))

ano = date.today().year

cat = ano - nasc

if cat < 10:
    print('Mirin')
elif cat > 9 and cat < 15:
    print('INFANTIL')
elif cat > 14 and cat < 20:
    print('JUNIOR')
elif cat > 19 and cat < 21:
    print('SÊNIOR')
elif cat > 20:
    print('MASTER')