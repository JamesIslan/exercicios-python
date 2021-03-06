#Tratamento de erro incluso
def contador(inicio:int, fim:int, passo:int):
    if fim > inicio:
        numeros = list(range(inicio, fim + 1))
    else:
        numeros = list(range(fim, inicio+1))[::-1]
    print(f'Contagem de {inicio} a {fim}: ')
    print(*numeros[::passo], sep='  ')
    print('Fim da contagem',)
    print('')


inicio = fim = passo = int()

contador(1, 10, 1)
contador(10, 0, 2)

print('Contagem personalizada:')

while True:
    try:
        inicio = int(input('Inicio da contagem: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

while True:
    try:
        fim = int(input('Fim da contagem:'))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

while True:
    try:
        passo = int(input('Passo da contagem: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

contador(inicio, fim, passo)