preco = float(input('Digite o preço do produto: \n'))
cond = int(input('Digite o número da opção de pagamento escolhida : \n 1 - á vista(dinheiro/cheque) \n 2 - á vista(cartão) \n 3 - 2x no cartão \n 4 - 3x ou mais no cartão \n '))

if cond == 1:
    total = preco - (preco * 0.10) 
elif cond == 2:
    total = preco - (preco * 0.05)
elif cond == 3:
    pass
elif cond == 4:
    total = preco + (preco * 0.20)
print('o total fica R${:.2f}'.format(total))