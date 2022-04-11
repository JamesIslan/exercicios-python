fatores = []
num = int(input('Digite aqui um número inteiro: '))
for divisor in range(1, num + 1):
    if num % divisor == 0:
        fatores += [divisor]
if fatores == [1, num]:
    print(f'{num} é um número primo')
else:
    print(f'{num} não é um número primo')

