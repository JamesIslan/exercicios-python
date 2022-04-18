#Tratamento de erro incluso
lista = list()

for i in range(7):
    while True:
        try:
            valor = int(input('Digite aqui um número inteiro: '))
            lista += [valor]
            break
        except ValueError:
            print('Digite um valor válido!')
            continue

pares = list(sorted(filter(lambda x: x % 2 == 0, lista)))
impares = list(sorted(filter(lambda x: x % 2 == 1, lista)))

print('-='*35)
print(f'Os números pares digitados foram: {str(pares)[1:-1]}')
print(f'Os números ímpares digitados foram: {str(impares)[1:-1]}', sep=', ')
print('-='*35)