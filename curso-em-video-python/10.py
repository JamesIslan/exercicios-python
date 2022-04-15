# Tratamento de erro incluso

while True:
    try:
        carteira = float(input(f'Digite aqui a quantia em Reais (R$): '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue
print(
    f'O valor de R$ {carteira:.2f} equivale a US$ {float(carteira) / float(5.54):.2f}')
