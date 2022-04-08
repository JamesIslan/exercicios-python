resultado = 0
for numero in range(1, 501):
    if numero % 3 == 0:
        resultado += numero
print(f'A soma de todos os valores múltiplos de 3 no intervalo entre 1 e 500 é {resultado}')