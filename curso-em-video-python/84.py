# Tratamento de erro incluso
pessoas = list()
continua = str()

while continua != 'N':
    nome = str(input('Digite aqui o nome da pessoa: ')).capitalize().strip()
    while True:
        try:
            peso = float(input('Digite aqui o peso da pessoa:'))
            pessoas += [[nome, peso]]
            break
        except ValueError:
            print('Digite um peso válido!')
            continue
    while True:
        continua = str(input('Deseja inserir outros valores? (S/N): ')).upper()
        if continua == 'S' or continua == 'N':
            print('-=' * 25)
            break
        else:
            print('Digite um valor válido!')
            continue

filtro = list((item[1] for item in (sublista for sublista in pessoas)))

x = (dupla[0] for dupla in (sublista for sublista in pessoas)
     if dupla[1] == max(filtro))
y = (dupla[0] for dupla in (sublista for sublista in pessoas)
     if dupla[1] == min(filtro))

print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')

print(f'O menor peso foi de {min(filtro)}. Esse é o peso de: ', end='')
print(*list(y), sep=', ')

print(f'O maior peso foi de {max(filtro)}. Esse é o peso de: ', end='')
print(*list(x), sep=', ')
