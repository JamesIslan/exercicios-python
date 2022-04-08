import random
opcoes = ["pedra", "papel", "tesoura"]
computador = random.choice(opcoes)
usuario = str(input('Pedra, Papel ou Tesoura?')).lower()
if usuario not in opcoes:
    exit()
print(f"O computador escolheu {computador.capitalize()}\nO usuário escolheu {usuario.capitalize()}\n{print('O computador VENCEU') if computador == 'pedra' and usuario == 'tesoura' or computador == 'papel' and usuario == 'pedra' or computador == 'tesoura' and usuario == 'papel' else print('Houve um empate') if computador == usuario else print('O usuario VENCEU')}")