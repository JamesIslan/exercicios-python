ano = int(input('Digite aqui um ano qualquer: '))
if len(str(ano)) > 4:
    print('Digite um ano válido')
elif ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é um ano bissexto.')
else:
    print(f'{ano} não é um ano bissexto.')
