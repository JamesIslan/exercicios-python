vitorias = 0
from random import randint as aleatorio
print(f'{"=-"*50}')
print('Vamos jogar par ou ímpar!')
print(f'{"=-"*50}')
while True:
    computador = aleatorio(0, 10)
    jogador_valor = int(input('Digite um número entre 0 e 10: '))
    soma = computador + jogador_valor
    jogador_par_impar = str(input('Par ou ímpar? (P/I): ')).upper()
    print(f'Você jogou {jogador_valor} e o computador jogou {computador}. Resultado:{soma}')
    resultado = "P" if soma % 2 == 0 else "I"
    if jogador_par_impar == resultado:
        print('Você Venceu!')
        vitorias += 1
        continue
    else:
        print('Você Perdeu!')
        print(f'Total de vitórias:{vitorias}')
        break