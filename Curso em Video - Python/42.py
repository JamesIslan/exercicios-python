seg1 = int(input('Digite aqui o valor do segmento "A": '))
seg2 = int(input('Digite aqui o valor do segmento "B": '))
seg3 = int(input('Digite aqui o valor do segmento "C": '))

if (seg1 + seg2 > seg3) and (seg2 + seg3 > seg1) and (seg1 + seg3 > seg2):
    print(f'É POSSÍVEL DE SE MONTAR UM TRIANGULO COM ESSES VALORES.')
    if (seg1 == seg2 == seg3):
        print('Esse triângulo é do tipo EQUILÁTERO')
    elif (seg1 == seg2) or (seg1 == seg3) or (seg2 == seg3):
        print('Esse triângulo é do tipo ISOSCELES')
    else:
        print('Esse triângulo é do tipo ESCALENO')
else:
    print(f'NÃO É POSSÍVEL DE SE MONTAR UM TRIÂNGULO COM ESSES VALORES.')