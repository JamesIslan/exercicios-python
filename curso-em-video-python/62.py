termo = int(input('Digite aqui o primeiro termo da progressão: '))
progressao = int(input('Digite aqui a progressão: '))
qtd_termos = 0
termos = 10
print(termo)
while qtd_termos < termos:
    qtd_termos += 1
    termo += progressao
    print(termo)
    if qtd_termos == (termos - 1):
        termos = int(
            input('Quantos mais termos deseja exibir? (0 para fechar): ')) + 1
        if termos == 1:
            break
        else:
            qtd_termos = 0
            continue
