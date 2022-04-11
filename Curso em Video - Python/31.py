distancia = float(input('Digite aqui a distância da viagem (Km): '))
if distancia <= 200:
    passagem = 0.50 * distancia
    print(f'Sua passagem custará R${passagem:.2f}')
else:
    passagem = 0.45 * distancia
    print(f'Sua passagem custará R${passagem:.2f}')