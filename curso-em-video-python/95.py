#Tratamento de erro incluso
lista_jogadores = list()
qtd_partidas = int()
dicionario = {'nome': str(), 'gols': list(), 'total': int()}
dicionario2 = {'nome': str(), 'gols': list(), 'total': int()}
while True:
    while True:
        dicionario['nome'] = str(input('Nome do jogador: ')).capitalize()
        if not (dicionario['nome'].isalpha()
                or dicionario['nome'].__contains__(' ')):
            print('Digite um valor válido!')
            continue
        else:
            break
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
                dicionario['gols'] += [(int(input(f'Gols no {num+1} jogo: ')))]
                break
            except ValueError:
                print('Digite um valor válido!')
                continue

    dicionario['total'] = sum(dicionario['gols'])

    while True:
        continua = str(input('Deseja continuar? (S/N): ')).upper()
        if (not continua.isalpha()) or (continua not in 'SN'):
            print('Digite uma opção válida!')
            continue
        else:
            break
    lista_jogadores.append(dicionario.copy())
    '''print(lista_jogadores)
    print(dicionario)'''
    dicionario['gols'] = []
    dicionario = dicionario2
    print('-' * 50)
    if continua == 'S':
        continue
    else:
        break

print("{:<10} {:<10} {:<25} {:<20}".format('Indice', 'Nome', 'Gols', 'Total'))
for indice, jogador in enumerate(lista_jogadores):
    print(
        "{:<10} {:<10} {:<25} {:<20}".format(
            str(indice), str(
                jogador['nome']), str(
                jogador['gols']), str(
                    jogador['total'])))
print('-=' * 40)
while True:
    mostrar_dados = str(
        input('Deseja mostrar os dados de algum jogador? (S/N): ')).upper()
    if mostrar_dados not in 'SN':
        print('Digite uma opção válida!')
        continue
    elif mostrar_dados == 'S':
        try:
            mostrar_dados = int(input('Digite o índice do jogador desejado: '))
        except ValueError:
            print('Digite um valor válido!')
            continue
        else:
            if mostrar_dados > len(lista_jogadores):
                print('Não há jogador com este índice em nosso cadastro!')
                continue
            else:
                jogador = lista_jogadores[mostrar_dados]
                print(f'Levantamento de {jogador["nome"]}')
                for num, value in enumerate(jogador['gols']):
                    print(
                        f'    No jogo {num+1}, {jogador["nome"]} fez {value} gols')
    else:
        break