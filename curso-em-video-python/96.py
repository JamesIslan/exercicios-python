#Tratamento de erro incluso
def area(lar : float, comp : float):
    area = lar * comp
    print(f'A área de um terreno {largura}m x {comprimento}m é de {area}m²')


largura = comprimento = float()

while True:
    try:
        largura = float(input('Digite a largura do terreno: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

while True:
    try:
        comprimento = float(input('Digite o comprimento do terreno: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

area(largura, comprimento)