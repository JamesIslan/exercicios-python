# Tratamento de erro incluso
while True:
    global preco_produto
    try:
        preco_produto = float(input('Digite aqui o valor do produto: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

reajuste = 5 / 100
novo_preco = "{:.2f}".format(preco_produto + (preco_produto * reajuste))
print(f'O novo valor do produto é de {"R$" + str(novo_preco)}')
