salario = float(input('Digite aqui o seu salário: '))
if salario > 1250:
    print(f'Seu salário com 10% de aumento resulta em R${(salario * 1.10):.2f}')
else:
    print(f'Seu salário com 15% de aumento resulta em R${(salario * 1.15):.2f}')