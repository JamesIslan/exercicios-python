peso = float(input('Digite aqui o seu peso (Kg): '))
altura = float(input('Digite aqui a sua altura (M): '))

imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('Você se encontra ABAIXO DO PESO')
elif 18.5 < imc < 25:
    print('Você se encontra com peso NORMAL')
elif 25 < imc < 30:
    print('Você se encontra com SOBREPESO')
elif 30 < imc < 40:
    print(f'Você se encontra em estado de OBESIDADE')
else:
    print(f'Você se encontra em estado de OBESIDADE MÓRBIDA')
