while True:
    sexo = str(input('Digite aqui o sexo de uma pessoa (M / F)')).upper()
    if (sexo != 'M') and (sexo != 'F'):
        print('Digite um sexo válido!')
    else:
        print('FIM DO PROGRAMA')
        break