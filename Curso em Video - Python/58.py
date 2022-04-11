from random import randint
numero = randint(0,10)
tentativas = 0
palpite = int()
while True:
    palpite = int(input('Digite aqui o seu palpite: '))
    tentativas += 1
    if palpite != numero:
        print('Você errou! Tente novamente.')
    else:
        print('Parabéns, você acertou!')
        print(f'Foram necessárias {tentativas} até que você acertasse')
        break