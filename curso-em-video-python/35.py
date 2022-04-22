seg1 = int(input('Digite aqui o valor do segmento "A": '))
seg2 = int(input('Digite aqui o valor do segmento "B": '))
seg3 = int(input('Digite aqui o valor do segmento "C": '))

if (seg1 + seg2 > seg3) and (seg2 + seg3 > seg1) and (seg1 + seg3 > seg2):
    print(f'É POSSÍVEL DE SE MONTAR UM TRIANGULO COM ESSES VALORES.')
else:
    print(f'NÃO É POSSÍVEL DE SE MONTAR UM TRIÂNGULO COM ESSES VALORES.')
