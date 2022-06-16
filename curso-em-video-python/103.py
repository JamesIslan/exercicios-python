# Tratamento de erro incluso
def ficha(nome: str = '<desconhecido>', gols: int = int()):
    print(f'O jogador {nome} fez {gols} gols no campeonato.')


while True:
    nome = str(input('Nome do Jogador: ')).capitalize()
    if not (nome.isalpha() or nome.__contains__(' ')):
        print('Digite um valor válido!')
        continue
    else:
        break

while True:
    global gols
    try:
        gols = int(input('Quantidade de gols: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

ficha(nome, gols)