num1 = int(input('Digite aqui um número inteiro: '))
num2 = int(input('Digite aqui outro número inteiro: '))

if num1 > num2:
    print(f'{num1} é o maior número\n{num2} é o menor número')
elif num1 < num2:
    print(f'{num2} é o maior número\n{num1} é o menor número')
else:
    print(f'Não há maior valor pois {num1} e {num2} são iguais')
