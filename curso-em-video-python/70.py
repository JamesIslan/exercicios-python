produtos_nome = []
produtos_preco = []
while True:
    nome = str(input("Digite aqui o nome do produto: "))
    preco = int(input("Digite aqui o preço do produto: "))
    produtos_nome += [nome]
    produtos_preco += [preco]
    continua = str(input('Deseja continuar?(S/N): ')).upper()
    if continua == "S":
        continue
    if continua == "N":
        print(f'Foram gastos R${sum(produtos_preco)} no total')
        print(f'{len(list(filter(lambda x: x > 1000, produtos_preco)))} dos produtos têm um valor superior a R$1000')
        print(
            f'O produto mais barato é {produtos_nome[produtos_preco.index(min(produtos_preco))]}')
        break
