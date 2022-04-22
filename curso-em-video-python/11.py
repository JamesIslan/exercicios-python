#Tratamento de erro incluso

area_parede, altura_parede, largura_parede = float(), float(), float()

while True:
    while True:
        try:
            altura_parede = float(input('Digite aqui a altura da parede: '))
            break
        except ValueError:
            print('Digite um valor válido!')
    while True:
        try:
            largura_parede = float(input('Digite aqui a largura da parede: '))
            break
        except ValueError:
            print(f'Digite um valor válido!')
            continue
    break
area_parede = altura_parede * largura_parede
cobertura_litro = 2
print(f'A área da parede são de {area_parede:.2f} M²')
print(f'São necessários {(area_parede / cobertura_litro):.2f} litros para pintar a parede')
