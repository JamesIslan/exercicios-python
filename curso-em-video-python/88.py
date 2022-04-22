#Tratamento de erro incluso
from random import shuffle

print('-='*30)
print(f'{"SORTEADOR MEGA SENA" : ^50}')
print('-='*30)

numeros = list(range(1,60))
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

for jogo in range(qtd_jogos):
    shuffle(numeros)
    print(f'Jogo {jogo+1}: {numeros[0:6]}')

print('-='*12, end=' ')
print('BOA SORTE!', end=' ')
print('-='*12)

