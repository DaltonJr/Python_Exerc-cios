r1 = int(input('Digite a comprimenta da reta 1: \n'))
r2 = int(input('Digite a comprimenta da reta 2: \n'))
r3 = int(input('Digite a comprimenta da reta 3: \n'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo')  
else:
    print('Os segmentos acima não podem formar um triângulo')