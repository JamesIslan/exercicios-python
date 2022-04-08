valor_produto = float(input('Digite aqui o valor do produto (R$): '))
print('Métodos de pagamento:'
      '\n1 - À vista em espécie ou cheque'
      '\n2 - À vista no cartão'
      '\n3 - Parcelado em 2x no cartão'
      '\n4 - Parcelado em 3x ou mais no cartão')
metodo_pagamento = int(input('Digite aqui o método de pagamento desejado: '))

if metodo_pagamento == 1:
    desconto = 0.10
    print(f'O valor final do produto será de R${valor_produto - (valor_produto * desconto)}')
elif metodo_pagamento == 2:
    desconto = 0.05
    print(f'O valor final do produto será de R${valor_produto - (valor_produto * desconto)}')
elif metodo_pagamento == 3:
    print(f'Você realizar o pagamento em 2x de R${(valor_produto / 2):.2f}')
    print(f'O valor final do produto será de R${valor_produto}')
elif metodo_pagamento == 4:
    parcelas = int(input('Em quantas parcelas você deseja pagar?: '))
    acrescimo = 0.20
    print(f'O valor final do produto será de R${valor_produto + (valor_produto * acrescimo)}')
    print(f'De forma parcelada, você irá pagar {parcelas} prestações de R${(valor_produto + (valor_produto * acrescimo)) / parcelas} cada')
else:
    print('Opção INVÁLIDA!')