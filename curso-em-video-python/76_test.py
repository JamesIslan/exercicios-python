tupla = ()
qtd_repeticoes = int(input("Quantos produtos você deseja contabilizar?: "))
for i in range(qtd_repeticoes):
    tupla += (str(input("Digite aqui o nome do produto: ")
                  ).capitalize(), float(input("Digite o preço: ")))
print("=" * 60)
print(f'{"Lista de Preços":^60}')
print("=" * 60)
for i in range(0, qtd_repeticoes * 2, 2):
    print(f'{tupla[i] + " ":.<50}', end=" R$")
    print(f'{(tupla[i + 1]):.2f}')
