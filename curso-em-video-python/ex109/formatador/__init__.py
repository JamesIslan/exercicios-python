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
