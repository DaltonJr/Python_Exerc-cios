nota1 = float(input('digite a primeira nota: \n'))
nota2 = float(input('digite a segunda nota: \n'))

media = (nota1 + nota2) / 2

if media < 5:
    print('REPROVADO')
elif media >= 5 and media < 7:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')

print('a média das notas {} e {}, é {:.1f}'.format(nota1,nota2,media))