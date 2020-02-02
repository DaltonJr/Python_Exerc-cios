from random import shuffle

nome1 = input("Digite um nome: ")
nome2 = input("Digite um nome: ")
nome3 = input("Digite um nome: ") 
nome4 = input("Digite um nome: ")

lista = [nome1,nome2,nome3,nome4]

shuffle(lista)

print('o aluno sorteado é {}'.format(lista))