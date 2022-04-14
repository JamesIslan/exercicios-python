print(
    f'''
    {"BEM-VINDO AO NOSSO BANCO!"}
    '''
)
valor = int(input('Digite aqui o valor a ser sacado: '))
qtd_50, qtd_20, qtd_10, qtd_1 = int(), int(), int(), int()
while True:
    if valor % 50 == 0:
        valor -= 50
        qtd_50 += 1
    elif valor % 20 == 0:
        valor -= 20
        qtd_20 += 1
    elif valor % 10 == 0:
        valor -= 10
        qtd_10 += 1
    elif valor % 1 == 0:
        valor -= 1
        qtd_1 += 1
    if valor == 0:
        print(
            f'''
    TOTAL DE CÉDULAS:
    {qtd_50} CÉDULAS DE R$50
    {qtd_20} CÉDULAS DE R$20
    {qtd_10} CÉDULAS DE R$10
    {qtd_1} CÉDULAS DE R$1
    "OBRIGADO E VOLTE SEMPRE!
            '''
        )
        break
