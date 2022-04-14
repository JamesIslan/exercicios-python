salario = float(input('Digite aqui o seu salário (R$): '))
aumento = 15 / 100
novo_salario = "{:.2f}".format(salario + (salario * aumento))
print(f'O seu novo salário é de {"R$" + str(novo_salario)}')
print('O seu novo salário é de {}'.format("R$" + str(novo_salario)))
