termo = int(input('Digite aqui o primeiro termo da progressão: '))
progressao = int(input('Digite aqui a progressão: '))
qtd_termos = 1
print(termo)
while qtd_termos < 10:
    qtd_termos += 1
    termo += progressao
    print(termo)