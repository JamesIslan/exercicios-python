
while True:
    global q
    try:
        q = int(input('Termos: '))
        break
    except ValueError:
        print('Digite um valor válido!')
        continue
termos = [0, 1, 1]
while len(termos) < q:
    termos.append(sum(termos[-2::]))
print(*termos, sep=', ')
