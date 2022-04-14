idades, lista, qtd_mulheres = 0, [], 0
for pessoa in range(1, 5):
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo: ').lower().strip()
    print('')
    idades += int(idade)
    if sexo == "masculino":
        lista += [nome, idade]
    if sexo == "feminino" and idade < 20:
        qtd_mulheres += 1
print(f'A média de idade é de {idades / 4} anos')
print(f'Existem {qtd_mulheres} mulheres com menos de 20 anos')
print(
    f'O homem mais velho é {lista[lista.index(max(lista[1::2])) - 1]} com {max(lista[1::2])} anos')
