# Tratamento de erro incluso
def notas(*iter: int | float | tuple | list, sit: bool = True):
    """
    -> Função feita para analisar conjunto de notas de alunos
    :param iter: variável composta ou conjunto de notas
    :param sit: Adiciona ao dicionário a situação geral dos alunos (Opcional)
    :return: Dicionário contendo maior nota, menor nota, média de notas e situação (caso requerido)
    """
    dicionario = dict()
    dicionario['notas'] = len(*iter)
    dicionario['maior'] = max(*iter)
    dicionario['menor'] = min(*iter)
    dicionario['media'] = sum(*iter) / len(*iter)
    if sit:
        if dicionario['media'] >= 7:
            dicionario['situação'] = 'BOA'
        elif 4.1 <= dicionario['media'] < 7:
            dicionario['situação'] = 'RAZOÁVEL'
        else:
            dicionario['situação'] = 'RUIM'
    return dicionario


lista_notas = []
while True:
    while True:
        try:
            nota = float(input('Digite a nota (Entre 0 e 10): '))
            if nota > 10:
                print('Digite uma nota entre 0 e 10!')
                continue
            lista_notas.append(nota)
            break
        except ValueError:
            print('Digite um valor válido!')
            continue

    while True:
        continua = str(input('Deseja continuar? (S/N): ')).upper()
        if continua not in 'SN':
            print('Digite um valor válido!')
            continue
        else:
            break
    if continua == 'S':
        continue
    else:
        break

func = notas(lista_notas)
print(func)
