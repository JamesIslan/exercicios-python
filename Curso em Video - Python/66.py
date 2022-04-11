soma = int()
qtd_numeros = int()
while True:
    numero = int(input('Digite um número (999 para parar): '))
    if numero == 999:
        print(f'Você digitou {qtd_numeros} números e a soma deles é {soma}')
        break
    else:
        soma += numero
        qtd_numeros += 1