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

print(f'A metade de {formatador.formatador(p)} é {formatador.metade(p, formatar=True)}')
print(f'O dobro de {formatador.formatador(p)} é {formatador.dobro(p, formatar=True)}')
print(f'Aumentando 10% em cima de {formatador.formatador(p)}, temos {formatador.aumentar(p, 10, formatar=True)}')
print(f'Diminuindo 13% em cima de {formatador.formatador(p)}, temos {formatador.diminuir(p, 13, formatar=True)}')
formatador.resumo(p, 10, 13)
