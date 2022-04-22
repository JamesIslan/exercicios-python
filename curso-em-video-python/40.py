nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = "{:.2f}".format((nota1 + nota2) / 2)

if float(media) < 5:
    print('Infelizmente você não atingiu a nota mínima para recuperação.'
          '\nSituação final: REPROVADO')
elif 5 < float(media) < 6.9:
    print('Você não atingiu a aprovação, mas poderá recuperar.'
          '\nSituação final: RECUPERAÇÃO')
else:
    print('Parabéns, sua nota é suficiente para a aprovação!'
          '\nSituação final: APROVADO')
