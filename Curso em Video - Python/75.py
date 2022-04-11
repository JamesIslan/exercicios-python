tupla = ()
qtd_pares = int()
for i in range(4):
    tupla += (int(input('Digite um valor inteiro: ')),)
for item in tupla:
    if item % 2 == 0:
        qtd_pares += 1
print(f'Você digitou os valores: {tupla}')
print(f'O número 9 aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 foi localizado na posição {tupla.index(3) + 1} da tupla')
else:
    print(f'Não foi possível identificar o número 3 na lista')
print(f'{qtd_pares} dos itens da tupla são pares')
