# Tratamento de erro incluso
def fatorial(num: int = int(), show: bool = bool()):
    calc = 1
    for i in range(num, 0, -1):
        if show:
            print(f'{calc} x {i} = {calc * i}')
        calc *= i
    print(f'O fatorial de {num} é {calc}')
    return calc


while True:
    global numero
    try:
        numero = int(input('Número: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

while True:
    mostrar = str(input('Mostrar cálculo? (S/N): ')).upper()
    if mostrar not in 'SN':
        print('Digite um valor válido!')
        continue
    elif mostrar == 'S':
        mostrar = True
    else:
        mostrar = False
    break

fatorial(numero, mostrar)
