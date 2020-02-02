from random import choice

nome1 = input("Digite um nome: ")
nome2 = input("Digite um nome: ")
nome3 = input("Digite um nome: ") 
nome4 = input("Digite um nome: ")

sort = choice([nome1,nome2,nome3,nome4])

print('o aluno sorteado é {}'.format(sort))