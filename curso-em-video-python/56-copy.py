import operator
idades = 0
lista_homens = {}
for pessoa in range(1, 5):
    pessoa_nome = str(input('Digite aqui o nome da pessoa: ')
                      ).capitalize().strip()
    pessoa_idade = int(input('Digite aqui a idade da pessoa: '))
    pessoa_sexo = str(
        input('Digite aqui o sexo da pessoa (Masculino / Feminino): ')).lower().strip()
    print('')
    if pessoa_sexo == "masculino":
        lista_homens = {**lista_homens, pessoa_nome: pessoa_idade}
    idades += int(pessoa_idade)
lista_homens_inversa = sorted(
    lista_homens.items(),
    key=operator.itemgetter(1),
    reverse=True)
print(f'A média de idade do grupo é de {idades / 4} anos')
print('Duas pessoas possuem a mesma idade')
print(
    f'O homem mais velho é {(lista_homens_inversa[0])[0]} com {(lista_homens_inversa[0])[1]} anos')
