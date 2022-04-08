while True:
    numero = int(input('Digite um número para ver sua tabuada: '))
    if numero < 0:
        print('Você digitou um valor negativo. Parando programa...')
        break
    print(f'{"-"*40}')
    for n in range(10):
        print(f'{numero} x {n} = {numero * n}')
    print(f'{"-"*40}')
