# Tratamento de erro incluso
while True:
    try:
        numero = int(input("Digite aqui um número inteiro: "))
    except ValueError:
        print(f'Digite apenas números inteiros!\n')
        continue
    antecessor = numero - 1
    sucessor = numero + 1
    print(f'O antecessor de {numero} é {antecessor}, e o sucessor de {numero} é {sucessor}')
