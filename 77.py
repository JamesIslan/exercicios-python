tupla = ()
qtd_palavras = int(input("Quantas palavras você deseja exibir? "))

for i in range(qtd_palavras):
    tupla += (input("Digite aqui a palavra: ").lower(),)
for palavra in tupla:
    print(f'A palavra {palavra} tem as vogais: ', end="")
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end='')
    print()
