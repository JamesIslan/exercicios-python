# Tratamento de erro incluso
continua = str()
while continua != 'n':
      try:
            numero = int(input('Digite aqui um número inteiro: '))
      except ValueError:
            print('Digite apenas números inteiros!\n')
            continue
      print(f'A tabuada deste número é: ')
      print(f' {numero*1}, '
            f'\n {numero*2}, '
            f'\n {numero*3}, '
            f'\n {numero*4}, '
            f'\n {numero*5}, '
            f'\n {numero*6}, '
            f'\n {numero*7}, '
            f'\n {numero*8}, '
            f'\n {numero*9}.')
      while True:
            continua = str(input('Deseja ver a tabuada de outro número? (S/N): ')).lower()
            if continua not in 'sn':
                  print('Digite uma opção válida!\n')
                  continue
            else:
                  break