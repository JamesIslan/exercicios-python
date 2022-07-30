def filecheck(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def filecreate(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    global a
    try:
        a = open(nome, 'rt')
    except FileNotFoundError:
        print('O arquivo não pode ser encontrado.')
    except:
        print('Erro ao ler o arquivo')
    else:
        for line in a:
            dado = line.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20}{dado[1]} anos')
        print(a.read())
    finally:
        a.close()


def cadastrar(arq: str):
    global a
    idade_cadastro = 0
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        while True:
            nome_cadastro = str(input('Nome: ')).strip()
            if nome_cadastro == '':
                nome_cadastro = 'Desconhecido'
                break
            elif not (nome_cadastro.isalpha() or nome_cadastro.__contains__(' ')):
                print('Digite um nome válido!')
                continue
            else:
                break
        while True:
            try:
                idade_cadastro = int(input('Idade: '))
                break
            except ValueError:
                print('Digite uma idade válida!')
                continue
        try:
            a.write(f'{nome_cadastro};{idade_cadastro}\n')
        except:
            print('Houve um ERRO ao escrever os dados!')
        else:
            print(f'Novo registro de {nome_cadastro} adicionado!')
    finally:
        a.close()
