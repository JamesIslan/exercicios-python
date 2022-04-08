expressao = str()
while True:
    expressao = str(input('Digite aqui a expressão: '))
    if '(' and ')' not in expressao:
        print('Digite uma expressão completa.')
        continue
    else:
        break
qtd_parenteses_abertos = expressao.count('(')
qtd_parenteses_fechados = expressao.count(')')
if qtd_parenteses_abertos == qtd_parenteses_fechados:
    print(f'Essa expressão está sintaticamente correta.')
else:
    print(f'Essa expressão está sintaticamente errada.')
    if qtd_parenteses_abertos > qtd_parenteses_fechados:
        print(f'A expressão não foi fechada corretamente.')
    elif qtd_parenteses_fechados > qtd_parenteses_abertos:
        print(f'A expressão não foi aberta corretamente.')
    if expressao.index('()'):
        print(f'Existem parênteses desnecessários nessa expressão.')
    else:
        print(f'Não existem parênteses desnecessários nessa expressão.')
