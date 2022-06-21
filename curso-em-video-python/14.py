# Tratamento de erro incluso
n = 1
par = impar = 0
while n != 0:
    while True:
        try:
            n = int(input('Digite um valor: '))
            break
        except ValueError:
            print('Digite um valor válido!')
            continue
    if n == 0:
        continue
    elif n % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Você digitou {par} números pares e {impar} números impares')
