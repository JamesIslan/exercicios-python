# Tratamento de erro incluso
global num


def leiaint(msg: str):
    global num
    while True:
        try:
            num = int(input(msg))
            break
        except (ValueError, TypeError):
            print('ERRO! Digite um valor inteiro válido!')
            continue
        except KeyboardInterrupt:
            num = 0
            print('\nO usuário preferiu não digitar esse número.')
            break
    return num


def leiafloat(msg: str):
    global num
    while True:
        try:
            num = float(input(msg))
            break
        except (ValueError, TypeError):
            print('ERRO! Digite um valor real válido!')
            continue
        except KeyboardInterrupt:
            num = 0
            print('\nO usuário preferiu não digitar esse número.')
            break
    return num


i = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número real: ')

print(f'O valor inteiro digitado foi {i} e o real foi {r}')
