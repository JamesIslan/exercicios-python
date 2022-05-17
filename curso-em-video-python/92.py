#Tratamento de erro incluso
from datetime import date

ano_atual = date.today().year
dicionario = dict()

while True:
    try:
        nome = str(input('Nome do usuário: ')).capitalize()
        dicionario['nome'] = nome
        break
    except ValueError:
        print('Digite um valor válido!')
        continue
while True:
    nascimento = int(input('Ano de nascimento: '))
    if nascimento < 1900:
        print('Digite um ano válido!')
        continue
    else:
        idade = ano_atual - nascimento
        dicionario['idade'] = idade
        break
while True:
    try:
        ctps = int(input('Número da Carteira de Trabalho (0 se não tiver): '))
        dicionario['ctps'] = ctps
        if ctps != 0:
            while True:
                try:
                    ano_contratacao = int(input('Ano de contratação: '))
                    dicionario['ano de contratação'] = ano_contratacao
                    break
                except ValueError:
                    print('Digite um valor válido!')
                    continue
            while True:
                try:
                    salario = float(input('Salário (R$): '))
                    dicionario['salário'] = f'{salario:.2f}'
                    break
                except ValueError:
                    print('Digite um valor válido!')
                    continue
        break
    except ValueError:
        print('Digite um valor válido!')
        continue
print('-='*60)
for k,v in dicionario.items():
    print(f'{k.capitalize()} tem o valor {v}')