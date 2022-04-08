valor_casa = float(input('Digite aqui o valor da casa: '))
salario = float(input('Digite aqui o valor do seu salário: '))
qtd_anos = int(input('Em quantos anos você deseja financiar a casa: '))

qtd_prestacoes = qtd_anos * 12
valor_prestacao = valor_casa / qtd_prestacoes

if valor_prestacao > (0.3 * salario):
    print(f'Infelizmente, você está inelegível para o financiamento ;(')
else:
    print(f'Parabéns, você está elegível para o financiamento!'
          f'\nVocê pagará {qtd_prestacoes} prestações de R${valor_prestacao:.2f} cada uma, durante {qtd_anos} ano(s)')