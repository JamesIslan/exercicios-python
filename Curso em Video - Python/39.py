from datetime import date

nascimento = int(input('Digite aqui o ano do seu nascimento '))
ano_atual = int(date.today().year)

if ano_atual - nascimento < 18:
    print(f'Você ainda não possui a idade necessária para se alistar.'
          f'\nDaqui a {18 - (ano_atual - nascimento)} anos você poderá tentar novamente')
elif ano_atual - nascimento == 18:
    print(f'Está na hora de se alistar!')
else:
    print(f'Você não está mais habilitado para alistamento '
          f'pois você está {(ano_atual - nascimento) - 18} anos atrasado')