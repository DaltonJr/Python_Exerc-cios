from math import hypot

cat1 = float(input('digite o valor do primeiro cateto: '))
cat2 = float(input('digite o valor do segundo cateto: '))

hip = hypot(cat1, cat2)

print('o comprimento da hipotenusa é {:.2f}'.format(hip))