def leiadinheiro(msg: str):
    while True:
        global valor
        valor = str(input(msg))
        try:
            return float(valor)
        except ValueError:
            if ',' in valor:
                try:
                    valor = valor.replace(',', '.')
                    return float(valor)
                except ValueError:
                    print('Insira um valor válido!')
                    continue
            else:
                print('Insira um valor válido!')
                continue