# Tratamento de erro incluso
while True:
    global salario
    try:
        salario = float(input('Digite aqui o seu salário (R$): '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

aumento = 15 / 100
novo_salario = "{:.2f}".format(salario + (salario * aumento))
print(f'O seu novo salário é de {"R$" + str(novo_salario)}')
