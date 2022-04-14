brasileirao = (
    'Atlético Mineiro',
    'Flamengo',
    'Palmeiras',
    'Fortaleza',
    'Corinthians',
    'Bragantino',
    'Fluminense',
    'América Mineiro',
    'Atlético Goianiense',
    'Santos',
    'Ceará',
    'Internacional',
    'Atlético Paranaense',
    'Cuiabá',
    'Juventude',
    'Grêmio',
    'Bahia',
    'Sport',
    'Chapecoense'
)
print(f'Os primeiros 5 colocados do Brasileirão 2021 são: {brasileirao[:5]}')
print(f'Os últimos 4 colocados do Brasileirão 2021 são: {brasileirao[-4:]}')
print(f'A lista organizada dos times é: ')
for time in sorted(brasileirao):
    print(time)
print(
    f'O time da Chapecoense está na posição {brasileirao.index("Chapecoense")+2}')
