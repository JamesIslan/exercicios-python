lista = []
for i in range(5):
    lista += [int(input(f"Digite um valor para a posição {i}: "))]
print(f'Os valores digitados foram: {str(lista)[1:-1]}')
print(f'O maior valor digitado foi {max(lista)}', end=' ')
if lista.count(max(lista)) == 1:
    print(f'e foi encontrado na posição {lista.index(max(lista))}')
else:
    print(f'aparecendo {lista.count(max(lista))} vezes nas posições: ', end='')
    for pos in list(enumerate(lista)):
        if pos[1] == max(lista):
            print(pos[0], end=' ')
print(f'\nO menor valor digitado foi {min(lista)}', end=' ')
if lista.count(min(lista)) == 1:
    print(f'e foi encontrado na posição {lista.index(min(lista))}')
else:
    print(f'aparecendo {lista.count(min(lista))} vezes nas posições: ', end='')
    for pos in list(enumerate(lista)):
        if pos[1] == min(lista):
            print(pos[0], end=' ')
