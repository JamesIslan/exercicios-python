def formatador(func):
    return str(f'R${func:.2f}').replace('.', ',')

def dobro(n: float = float(), formatar=True):
    operacao = n * 2
    if formatar:
        return formatador(operacao)
    else:
        return operacao


def metade(n: float = float(), formatar=True):
    operacao = n / 2
    if formatar:
        return formatador(operacao)
    else:
        return operacao


def aumentar(n: float = float(), p: float = float(), formatar=True):
    operacao = n + (n * p / 100)
    if formatar:
        return formatador(operacao)
    else:
        return operacao


def diminuir(n: float = float(), p: float = float(), formatar=True):
    operacao = n - (n * p / 100)
    if formatar:
        return formatador(operacao)
    else:
        return operacao


def resumo(n: float = float(), a: int = int(), d: int = int()):
    print('-'*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('-'*40)
    print(f'{"Preço analisado: ":<30}{formatador(n)}')
    print(f'{"Dobro do preço: ":<30}{dobro(n)}')
    print(f'{"Metade do preço: ":<30}{metade(n)}')
    print(f'{f"{a}% de aumento: ":<30}{aumentar(n, a)}')
    print(f'{f"{d}% de redução: ":<30}{diminuir(n, d)}')
    print('-' * 40)
