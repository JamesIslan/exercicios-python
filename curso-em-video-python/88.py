from random import choice, choices

print('-='*30)
print(f'{"SORTEADOR MEGA SENA" : ^50}')
print('-='*30)

lista = []
qtd_jogos = int()

while True:
    try:
        qtd_jogos = int(input('Quantos jogos você deseja sortear? '))
        break
    except ValueError:
        print('Digite apenas números inteiros!')
        continue

print('-='*10, end=' ')
print(f'{f"SORTEANDO {qtd_jogos} JOGOS"}', end=' ')
print('-='*10, end='\n')

for sorteio in range(qtd_jogos):
    while len(lista) != qtd_jogos:

    print(f'Jogo {sorteio+1}: {lista[sorteio]}')

print('-='*12, end=' ')
print('BOA SORTE!', end=' ')
print('-='*12)

