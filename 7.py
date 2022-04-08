# Tratamento de erro incluso
nota1, nota2 = float(), float()
continua = str()
while continua != 'n':
    try:
        nota1 = float(input("Digite aqui a primeira nota do aluno: "))
        nota2 = float(input("Digite aqui a segunda nota do aluno: "))
    except ValueError:
        print(f'Digite apenas números inteiros ou de ponto flutuante!')
        continue
    media_notas = float((nota1 + nota2) / 2)
    print(f'A média aritmética simples das duas notas é de {media_notas:.2f} pontos')
    while True:
        continua = str(input('Deseja fazer o cálculo de outra nota? (S/N): ')).lower()
        if continua not in 'sn':
            print('Digite uma opção válida!')
            continue
        else:
            break
