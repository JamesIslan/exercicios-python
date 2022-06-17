# Tratamento de erro incluso
def ajuda():
    from time import sleep
    while True:
        print('\033[1;30;42m', end='')
        print('-='*30, end='')
        print('\033[m')
        print('\033[1;30;42m', end='')
        print(f'{"BEM - VINDO AO NOSSO SISTEMA DE AJUDA!":^60}', end='')
        print('\033[m')
        print('\033[1;30;42m', end='')
        print('-='*30, end='')
        print('\033[m')
        sleep(0.5)
        comando = str(input('Digite o comando desejado > ')).lower()
        if comando == 'fim':
            break
        print('\n')
        print('\033[1;30;46m', end='')
        print(f"{'-='*30}", end='')
        print('\033[m')
        print('\033[1;30;46m', end='')
        print(f'{f"Acessando o comando {comando}":^60}', end='')
        print('\033[m')
        print('\033[1;30;46m', end='')
        print(f"{'-='*30}", end='')
        print('\033[m')
        help(comando)


ajuda()
