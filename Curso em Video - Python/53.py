palavra_inversa = ''
palavra = str(input('Digite aqui a palavra: ')).lower()
palavra_junta = palavra.replace(" ", '')
for letra in palavra_junta[::-1]:
    palavra_inversa += letra
if palavra_inversa == palavra_junta:
    print(f'{palavra.capitalize()} É UM PALÍNDROMO')
else:
    print(f'{palavra.capitalize()} NÃO É UM PALINDROMO')
