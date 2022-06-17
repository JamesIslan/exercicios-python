# Tratamento de erro incluso
import formatador

while True:
    global p
    try:
        p = float(input('Digite o preço (R$): '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

print(f'A metade de {formatador.formatador(p)} é {formatador.formatador(formatador.metade(p))}')
print(f'O dobro de {formatador.formatador(p)} é {formatador.formatador(formatador.dobro(p))}')
print(f'Aumentando 10% em cima de {formatador.formatador(p)}, temos {formatador.formatador(formatador.aumentar(p, 10))}')
print(f'Diminuindo 13% em cima de {formatador.formatador(p)}, temos {formatador.formatador(formatador.diminuir(p, 13))}')
