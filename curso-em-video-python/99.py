# Tratamento de erro incluso
def maior(*num: (int, float, list, tuple)):
    maior = max(*num)
    print(f'O maior número é {maior}')


valores = []

while True:
    while True:
        try:
            valores.append(input('Digite um valor: '))
            break
        except ValueError:
            print('Digite um valor válido!')
            continue
    while True:
        continua = str(input('Deseja continuar? (S/N): ')).upper()
        if continua not in 'SN':
            print('Digite um valor válido!')
            continue
        else:
            break
    if continua == 'S':
        continue
    else:
        break

maior(valores)