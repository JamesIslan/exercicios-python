# Tratamento de erro incluso
import moeda

while True:
    global p
    try:
        p = float(input('Digite o preço (R$): '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo 13%, temos {moeda.diminuir(p, 13)}')
