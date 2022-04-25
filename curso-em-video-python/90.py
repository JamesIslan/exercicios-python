# Tratamento de erro incluso
dicionario = dict()
while True:
    try:
        dicionario['nome'] = str(input('Digite aqui o nome do aluno: '))
        break
    except ValueError:
        print('Digite um valor válido')
        continue

while True:
    try:
        dicionario['media'] = float(input('Digite aqui a média do aluno: '))
        break
    except ValueError:
        print('Digite um valor válido')
        continue

dicionario['situacao'] = 'Aprovado' if dicionario['media'] >= 70 else 'Reprovado'

for k,v in dicionario.items():
    print(f'{k.capitalize()} é {v}')