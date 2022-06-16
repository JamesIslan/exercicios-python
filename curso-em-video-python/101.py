# Tratamento de erro incluso
def voto(nasc: int = int()):
    from datetime import date
    idade = date.today().year - nasc
    if 18 <= idade <= 64:
        status = 'OBRIGARÓRIO'
    elif (16 <= idade <= 17) or (idade >= 65):
        status = 'OPCIONAL'
    else:
        status = 'NEGADO'
    print(f'Com {idade} anos, VOTO {status}.')


while True:
    global nascimento
    try:
        nascimento = int(input('Ano de nascimento: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

voto(nascimento)
