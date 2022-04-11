from random import randint as aleatorio
numero = aleatorio(0,5)
palpite = int(input('Digite aqui o seu palpite: '))
print('VOCÊ ACERTOU' if palpite == numero else 'VOCÊ ERROU')