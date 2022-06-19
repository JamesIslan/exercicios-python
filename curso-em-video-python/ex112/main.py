# Tratamento de erro incluso
from utilidadescev import formatador, dado

while True:
    global p
    try:
        p = dado.leiadinheiro('Digite o preço (R$) :')
        break
    except ValueError:
        print('Digite um valor válido!')
        continue

formatador.resumo(p, 35, 22)

