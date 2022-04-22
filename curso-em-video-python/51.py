termo = int(input('Digite aqui o primeiro termo da progressão: '))
progressao = int(input('Digite a constante de progressão aritmética: '))
print(termo)
for numero in range(0, 9):
    termo += progressao
    print(termo)
