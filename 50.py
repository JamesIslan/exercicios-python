soma = 0
cont = 0
for numero in range(0, 6):
    numeros = int(input('Digite aqui um número: '))
    if numeros % 2 == 0:
        soma += numeros
        cont += 1
print(f'Você informou {cont} {"número PAR" if cont == 1 else "números PARES"} e a soma resultou em {soma}')