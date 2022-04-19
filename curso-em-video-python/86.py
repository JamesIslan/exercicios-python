# Tratamento de erro incluso
lista = []

for i in range(3):
    while len(lista) != 3:
        try:
            lista += \
                [[
                    int(input('Digite um valor numérico: ')),
                    int(input('Digite um valor numérico: ')),
                    int(input('Digite um valor numérico: '))
                ]]
        except ValueError:
            print('Digite um valor válido!')
            continue
    print('\n', *list([num] for num in lista[i]), sep=' ')
