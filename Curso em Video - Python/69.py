qtd_homens = int()
mais18 = int()
mulheres_menos20 = int()
while True:
    sexo = str(input('Digite aqui o sexo da pessoa (Masculino/Feminino): ')).capitalize()
    if sexo == "Masculino" or sexo == "Feminino":
        idade = int(input('Digite aqui a idade da pessoa: '))
        if idade > 18: mais18 += 1
        if sexo == "Masculino": qtd_homens += 1
        elif sexo == "Feminino" and idade < 20: mulheres_menos20 += 1
        continua = str(input('Deseja continuar? (S/N): ')).upper()
        if continua == "S": continue
        elif continua == "N":
            print(f'Foram cadastrados {qtd_homens} homens')
            print(f'Foram cadastrados {mais18} pessoas maiores de 18 anos')
            print(f'Foram cadastrados {mulheres_menos20} mulheres com menos de 20 anos')
            break
