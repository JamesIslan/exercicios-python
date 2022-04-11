num = int(input('Digite um número: '))
fator = 1
resultado = 1
while fator < (num+1):
    resultado = resultado * fator
    fator += 1
print(f'O fatorial de {num} é {resultado}')