numero = int(input('Digite aqui o número para ser convertido: '))
print('''Escolha uma das bases para fazer a conversão:
[ 1 ] - Converter para BINÁRIO
[ 2 ] - Converter para OCTAL
[ 3 ] - Converter para HEXADECIMAL

''')

escolha = int(input('Digite aqui a opção desejada: '))

if escolha == 1:
    print(f'A conversão de {numero} para binário é {bin(numero)[2:]}')
elif escolha == 2:
    print(f'A conversão de {numero} para octal é {oct(numero)[2:]}')
elif escolha == 3:
    print(f'A conversão de {numero} para hexadecimal é {hex(numero)[2:]}')
else:
    print('Digite uma opção válida!')