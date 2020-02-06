r1 = int(input('Digite a comprimenta da reta 1: \n'))
r2 = int(input('Digite a comprimenta da reta 2: \n'))
r3 = int(input('Digite a comprimenta da reta 3: \n'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo')  
    if r1 == r2 and r1 == r3:
        print('Equilatero')
    elif (r1 == r2 or r1 == r3 or r2 == r3)and(r1 != r2 or r1 != r3 or r2 != r3) :
        print('Isóceles')
    elif r1 != r2 and r1 != r3:
        print('Escaleno')
else:
    print('Os segmentos acima não podem formar um triângulo')

