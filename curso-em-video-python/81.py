continua = str()
lista = []
while continua != 'n':
    lista += [int(input('Digite aqui um número: '))]
    while True:
        continua = str(input('Deseja adicionar outro número? (S/N): ')).lower()
        if continua not in 'sn':
            print('Digite uma opção válida:')
            continue
        else:
            break
print(f'Você digitou ao todo {len(lista)} números')
print(
    f'A lista de números em ordem decrescente é: {sorted(lista, reverse=True)}')
if 5 in lista:
    if lista.count(5) == 1:
        print(
            f'O valor 5 foi digitado e se encontra na posição {lista.index(5)}na lista')
    else:
        print(
            f'O valor 5 foi digitado {lista.count(5)} vezes nas posições:',
            end=' ')
        for pos in list(enumerate(lista)):
            if pos[1] == min(lista):
                print(pos[0], end=' ')
else:
    print(f'O número 5 não foi encontrado na lista')
