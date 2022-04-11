nome = input('Digite aqui o seu nome completo: ')
if (nome.isupper()) or (nome.islower()):
    print('Digite seu nome de forma capitalizada (Inicial maiúscula e restante minúsculo)')
    exit()
else:
    nome_maiusculo = nome.upper()
    print(f'O seu nome escrito em maiúsculo é {nome_maiusculo}')
    nome_minusculo = nome.lower()
    print(f'O seu nome escrito em minúsculo é {nome_minusculo}')
    len_nome = nome.replace(" ", "")
    print(f'O seu nome possui {len(len_nome)} letras')
    primeiro_nome = nome.split()
    print(f'O seu primeiro nome é "{primeiro_nome[0]}"')

