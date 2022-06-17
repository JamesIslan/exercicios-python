def dobro(n: float = float()):
    operacao = n * 2
    return operacao


def metade(n: float = float()):
    operacao = n / 2
    return operacao


def aumentar(n: float = float(), p: float = float()):
    operacao = n + (n * p / 100)
    return operacao


def diminuir(n: float = float(), p: float = float()):
    operacao = n - (n * p / 100)
    return operacao
