import random
opcoes = ["Pedra", "Papel", "Tesoura"]

computador = random.choice(opcoes)
usuario = str(input('Pedra, Papel ou Tesoura?')).capitalize()
if usuario not in opcoes:
    print('Digite uma opção válida!')
print(f'O computador escolheu {computador.capitalize()}\nO usuário escolheu {usuario.capitalize()}')

if computador == opcoes[0] and usuario == opcoes[1]:
    print(f'Você venceu! O computador escolheu {computador}')
elif computador == opcoes[0] and usuario == opcoes[2]:
    print(f'O computador venceu! Ele escolheu {computador}')
elif computador == opcoes[1] and usuario == opcoes[0]:
    print(f'O computador venceu! Ele escolheu {computador}')
elif computador == opcoes[1] and usuario == opcoes[2]:
    print(f'Você venceu! O computador escolheu {computador}')
elif computador == opcoes[2] and usuario == opcoes[0]:
    print(f'Você venceu! O computador escolheu {computador}')
elif computador == opcoes[2] and usuario == opcoes[1]:
    print(f'O computador venceu! Ele escolheu {computador}')
else:
    print('Houve um empate!')