velocidade_carro = float(input('Digite aqui a velocidade do carro (KM/h): '))
if velocidade_carro > 80:
    print('Você foi multado por estar acima da velocidade')
    print(f'Sua multa foi de {"R$" + str(((int(velocidade_carro) - 80) * 7))}')