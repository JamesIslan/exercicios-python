soma, qtd_numeros, numeros = int(), int(), []
while True:
    numero = int(input('Digite um número: '))
    numeros += [numero]
    soma += numero
    qtd_numeros += 1
    continua = str(input('Deseja digitar outro número? (S/N) :')).upper()
    if continua == 'S':
        continue
    elif continua == 'N':
        print(f'Você digitou {qtd_numeros} números e a média deles é {soma / qtd_numeros}')
        print(f'O maior número digitado foi {max(numeros)}')
        print(f'O menor número digitado foi {min(numeros)}')
        break
    else:
        print('Digite um valor válido!')
        continue