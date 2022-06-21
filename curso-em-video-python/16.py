# Tratamento de erro incluso
from math import floor
while True:
    global numero
    try:
        numero = float(input("Digite aqui um número float (quebrado): "))
        if int(numero) == numero:
            print('Digite apenas números de ponto flutuante!')
            continue
        break
    except ValueError:
        print('Digite um valor válido!')
        continue
print(f'A parte inteira de {numero} é {floor(numero)}')
