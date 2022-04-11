while True:
    val1 = int(input('Digite aqui o primeiro valor: '))
    val2 = int(input('Digite aqui o segundo valor: '))
    print('''
    ESCOLHA UMA OPÇÃO
    [1] SOMAR AMBOS OS NÚMEROS
    [2] MULTIPLICAR AMBOS OS NÚMEROS
    [3] CALCULAR QUAL O MAIOR NÚMERO
    [4] DIGITAR NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ''')
    opcao = int(input('Digite o número da ação a ser realizado: '))
    if opcao == 1:
        print(f'A soma entre {val1} e {val2} é {val1 + val2}')
        break
    elif opcao == 2:
        print(f'O produto entre {val1} e {val2} é {val1 * val2}')
        break
    elif opcao == 3:
        print(f'Entre {val1} e {val2}, o maior número é {max(val1, val2)}')
        break
    elif opcao == 4:
        continue
    elif opcao == 5:
        exit('Você escolheu sair do programa')
    else:
        print('Digite uma opção válida!')