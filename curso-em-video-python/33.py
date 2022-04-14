num1 = int(input('Digite aqui um número: '))
num2 = int(input('Digite aqui mais um número: '))
num3 = int(input('Digite aqui outro número: '))

if (num1 > num2) and (num2 > num3):
    print(f'{num1} é o maior número \n{num3} é o menor número')
elif (num1 > num2) and (num3 > num1):
    print(f'{num3} é o maior número \n{num2} é o menor número')
elif (num2 > num1) and (num1 > num3):
    print(f'{num2} é o maior número \n{num3} é o menor número')
elif (num3 > num2) and (num2 > num1):
    print(f'{num3} é o maior número \n{num1} é o menor número')
elif (num2 > num1) and (num1 < num3):
    print(f'{num2} é o maior número \n{num1} é o menor número')
else:
    print(f'{num1} é o maior número \n{num2} é o menor número')
