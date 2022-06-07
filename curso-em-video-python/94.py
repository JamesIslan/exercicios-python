# Tratamento de erro incluso

dicionario = dict()
lista = list()

while True:
    while True:
        dicionario['nome'] = str(input('Nome da pessoa: ')).strip().capitalize()
        if not (dicionario['nome'].isalpha() or dicionario['nome'].__contains__(' ')):
            print('Digite um nome válido!')
            continue
        else:
            break

    while True:
        dicionario['sexo'] = str(input('Sexo (M/F): ')).strip().upper()
        if (not dicionario['sexo'].isalpha()) or (dicionario['sexo'] not in 'MF'):
            print('Digite um sexo válido!')
            continue
        else:
            break

    while True:
        try:
            dicionario['idade'] = int(input('Idade: '))
        except ValueError:
            print('Digite uma idade válida!')
        else:
            break

    lista += [dicionario.copy()]
    dicionario.clear()

    while True:
        continua = str(input('Deseja continuar? (S/N): ')).strip().upper()
        if (not continua.isalpha()) or (continua not in 'SN'):
            print('Digite uma opção válida!')
            continue
        else:
            break
    if continua == 'S':
        continue
    else:
        break

media_idade = float(f'{(sum(i["idade"] for i in lista) / len(lista)):.1f}')
lista_mulheres = list(f['nome'] for f in lista if f['sexo'] == 'F')
acima_media = list(i['nome'] for i in lista if i['idade'] > media_idade)
print('-=' * 50)
print(f'— O grupo tem {len(lista)} pessoas')
print(f'A média de idade do grupo é de {media_idade} anos')
if lista_mulheres:
    print(f'As mulheres cadastradas foram: {lista_mulheres}')
else:
    print(f'Nenhuma mulher foi cadastrada.')
if acima_media:
    print(f'As pessoas acima da média de idade são: {acima_media}')
else:
    print(f'Não há pessoas com idade acima da média')
