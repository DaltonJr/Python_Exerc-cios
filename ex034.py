sal = float(input('qual o salário do funcionário? \n'))

if sal > 1250:
    aum = sal + (sal * 0.10)
else:
    aum = sal + (sal * 0.15)
print('o salário com o reajuste é de R${}'.format(aum))    
