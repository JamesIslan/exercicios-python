continua = str()
lista = []
while continua != 'n':
    try:
        lista += [int(input('Digite um número inteiro: '))]
    except ValueError:
        print('Digite apenas números inteiros!')
        continue
    while True:
        continua = str(input('Deseja continuar? (S/N): ')).lower()
        if continua not in 'sn':
            print('Digite uma Opção Válida!')
            continue
        else:
            break
print(f'Você digitou os números:', end=' ')
print(str(lista)[1:-1])
print(f'Os números pares que você digitou foram:', end=' ')
print(str(list(filter(lambda x: x % 2 == 0, lista)))[1:-1])
print(f'Os números ímpares que você digitou foram:', end=' ')
print(str(list(filter(lambda x: x % 2 == 1, lista)))[1:-1])
