import datetime
idades = list(map(int, input('Digite aqui as idades (separados por espaço): ').split()))
maiores = 0
menores = 0
for ano in idades:
    if datetime.date.today().year - ano >= 18:
        maiores += 1
    else:
        menores += 1
print(f'{maiores} {"pessoa é maior de idade" if maiores == 1 else "pessoas são maiores de idade"} '
      f'e {menores} {"pessoa é menor de idade" if menores == 1 else "pessoas são menores de idade"}')