# Tratamento de erro incluso
continua = str()
while continua != 'n':
    try:
        valor_metros = float(input('Digite aqui o valor em metros: '))
    except ValueError:
        print(f'Digite apenas números inteiros ou de ponto flutuante!')
        continue
    conversao_centimetros = valor_metros * 100
    conversao_milimetros = conversao_centimetros * 10
    print(f'{valor_metros} equivale a {conversao_centimetros:.2f} centímetros ou {conversao_milimetros:.3f} milímetros')
    while True:
        continua = str(input(f'Deseja fazer outra conversão? (S/N)')).lower()
        if continua not in 'sn':
            print('Digite uma opção válida!')
            continue
        else:
            break
