valor = float(input('Qual o valor da casa: \n')) 
sal = float(input('Quanto é o salário: \n'))
anos = int(input('Em quantos anos será pago: \n'))

meses = anos * 12
maxp = sal * 0.30
pres = valor / meses

if pres > maxp:
    print('O valor da prestação excede o limite, prestação R${:.2f}, limiteR${:.2f}'.format(pres, maxp))
else:
    print('o valor da prestação está dentro do limite, prestação R${:.2f}, limiteR${:.2f}'.format(pres, maxp))