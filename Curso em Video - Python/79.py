lista = []
continua = str()
while True:
    num = int(input('Digite um número: '))
    if num in lista:
        print(f'O número {num} já existe na lista, portanto não será adicionado.')
    else:
        lista += [num]
        print(f'O número {num} foi adicionado à lista com sucesso!')
    continua = str(input('Deseja continuar? (S/N): ')).upper()
    if continua == "S":
        continue
    else:
        break
print(f'A sua lista possui os valores: {sorted(lista)}', sep=",")
