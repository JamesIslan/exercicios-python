idade = int(input('Digite aqui a sua idade: '))

if 0 < idade <= 9:
    print('Você se encaixa na categoria MIRIM!')
elif 10 <= idade <= 14:
    print('Você se encaixa na categoria INFANTIL!')
elif 15 <= idade <= 19:
    print('Você se encaixa na categoria JUNIOR!')
elif idade == 20:
    print('Você se encaixa na categoria SÊNIOR!')
else:
    print('Você se encaixa na categoria MASTER!')