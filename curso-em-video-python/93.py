#Tratamento de erro incluso
qtd_partidas = int()
dicionario, dicionario['nome'], dicionario['gols'], dicionario['total'] = dict(), str(), list(), int()

while True:
    try:
        dicionario['nome'] = str(input('Nome do jogador: ')).capitalize()
        break
    except ValueError:
        print('Digite um valor válido!')
        continue
while True:
    try:
        qtd_partidas = int(input('Quantidade de partidas: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

for num in range(qtd_partidas):
    while True:
        try:
            dicionario['gols'] += [int(input(f'Gols no {num+1} jogo: '))]
            break
        except ValueError:
            print('Digite um valor válido!')
            continue
dicionario['total'] = sum(dicionario['gols'])
print('-='*40)
print(dicionario)
print('-='*40)
for k,v in dicionario.items():
    print(f'O campo {k.capitalize()} tem o valor {v}')
print('-='*40)
print(f'O jogador {dicionario["nome"]} jogou {qtd_partidas} partidas.')
for num in range(qtd_partidas):
    print(f'\t=> Na partida {num+1}, fez {dicionario["gols"][num]} gols')
print(f'No total, o jogador fez {dicionario["total"]} gols')
