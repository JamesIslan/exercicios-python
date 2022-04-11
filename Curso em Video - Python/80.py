lista = [] # 6, 9, -10, -6, 8
for i in range(5):
    num = int(input('Digite um número: '))
    if i == 0:
        lista.append(num)
    else:
        for item in lista:
            if num < item:
                lista.insert(lista.index(item), num)
                break
            elif num > max(lista):
                lista.append(num)
                break
print(f'A lista de números que você digitou de forma crescente é: {f"{lista}"}', sep=',')