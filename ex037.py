n = int(input('Digite um número inteiro: '))
op = int(input('Escolha uma opção para a conversão e digite número referente: \n 1 - binário \n 2 - octal \n 3 - hexadecimal \n'))

if op == 1:
    print('{}'.format(bin(n)))    
elif op == 2:
    print('{}'.format(oct(n)))
elif op == 3:    
    print('{}'.format(hex(n)))
else:
    print('Opção inválida')    