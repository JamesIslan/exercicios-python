from filefunc import *

global selecao
global nome_cadastro
global idade_cadastro


def func(opcao: int, filename: str = ''):
    if opcao == 1:
        menu('PESSOAS CADASTRADAS')
        lerarquivo(filename)
    elif opcao == 2:
        menu('NOVO CADASTRO')
        cadastrar(filename)
    elif opcao == 3:
        menu('Saindo do sistema, até logo!')
    else:
        print('Digite um valor válido!')



def menu(msg: str):
    print('-' * 30)
    print(f'{msg.center(30)}')
    print('-' * 30)


"""def opcao():
    global selecao
    print(f'1 – Ver pessoas cadastradas\n'
          f'2 – Cadastrar nova Pessoa\n'
          f'3 – Sair do Sistema')
    print('-' * 30)
    while True:
        try:
            selecao = int(input('Sua Opção: '))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido!')
            continue
        else:
            if selecao not in [1, 2, 3]:
                print('ERRO! Digite uma opção válida')
                continue
            else:
                break
    return selecao"""


def opcao():
    global selecao
    while True:
        print(f'1 – Ver pessoas cadastradas\n'
              f'2 – Cadastrar nova Pessoa\n'
              f'3 – Sair do Sistema')
        print('-' * 30)
        while True:
            try:
                selecao = int(input('Sua Opção: '))
            except (ValueError, TypeError):
                print('ERRO! Digite um número inteiro válido!')
                continue
            else:
                if selecao not in [1, 2, 3]:
                    print('ERRO! Digite uma opção válida')
                    continue
                else:
                    break
        break
    return selecao
