# Tratamento de erro insluso
from filefunc import *
from modules import *

arq = 'arquivo.txt'
while True:
    if not filecheck(arq):
        filecreate(arq)
    menu('MENU PRINCIPAL')
    selecao = opcao()
    funcao = func(selecao, arq)
    if selecao == 3:
        break
    else:
        continue
