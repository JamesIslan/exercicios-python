altura_parede = float(input('Digite aqui a altura da parede: '))
largura_parede = float(input('Digite aqui a largura da parede: '))
area_parede = altura_parede * largura_parede
cobertura_litro = 2
print(f'São necessários {area_parede / cobertura_litro} litros para pintar a parede')