vel = int(input('Qual a velocidade do carro? '))

if vel > 80:
    print('Você ultrapassou a velocidade permitida!')
    print('Sua multa é de R${:.2f}'.format((vel - 80)* 7))
else:
    print('Você está dentro da velocidade permitida.')