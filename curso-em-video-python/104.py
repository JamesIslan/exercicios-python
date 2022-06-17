# Tratamento de erro incluso
def leiaint(msg: str):
    while True:
        num = input(msg)
        if not str(num).isnumeric():
            print('Digite um número inteiro válido')
            continue
        else:
            break
    return num


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
