produto1 = str(input('Digite aqui o nome do produto: ')).capitalize()
valor1 = "{:.2f}".format(
    float(input('Digite aqui o valor do produto anterior: ')))
produto2 = str(input('Digite aqui o nome do produto: ')).capitalize()
valor2 = "{:.2f}".format(
    float(input('Digite aqui o valor do produto anterior: ')))
produto3 = str(input('Digite aqui o nome do produto: ')).capitalize()
valor3 = "{:.2f}".format(
    float(input('Digite aqui o valor do produto anterior: ')))
tupla = (produto1, valor1, produto2, valor2, produto3, valor3)
print("=" * 50)
print(f'{"Lista de Preços":^50}')
print("=" * 50)
for i in range(0, 6, 2):
    print(tupla[i], end=" ")
    print("." * (60 - len(tupla[i])), end=" R$")
    print((tupla[i + 1]))
