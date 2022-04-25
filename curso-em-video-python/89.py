# Tratamento de erro incluso
lista = []
continua = str()

while continua != 'N':
    try:
        lista += \
            [[
                str(input('Digite o nome do aluno: ')).capitalize(),
                [float(input('Digite a primeira nota do aluno: ')),
                 float(input('Digite a segunda nota do aluno: '))]
            ]]
    except ValueError:
        print('Digite informações válidas!')
        continue
    while True:
        continua = str(input('Deseja digitar outro valor? (S/N): ')).upper()
        if continua not in 'SN':
            print('Digite uma opção válida!')
            continue
        else:
            print('')
            break
print(lista)

print('-=' * 20)
print(f'''
No.     NOME                MÉDIA
''')
print('-' * 40)
contador = (num for num in range(len(lista)))
for dados in lista:
    print(f'''
{next(contador):<4}    {dados[0]:<10}      {(sum(dados[1]) / 2):>8.1f}
    ''', end='\n')

while True:
    try:
        notas_aluno = int(input('Deseja mostras as notas de que aluno? (Valores não numéricos param o programa: '))
        if notas_aluno in list(range(len(lista))):
            print(f'As notas de {lista[notas_aluno][0]} foram: {lista[notas_aluno][1]}')
            print('-' * 70)
        else:
            print(f'Esse índice não consta em nosso cadastro!')
            continue
    except ValueError:
        break
