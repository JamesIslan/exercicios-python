numero = int(input('Digite aqui um número entre 0 e 9999: '))
if numero < 10:
    numero = "000" + str(numero)
    print(f'Esse número possui {numero[0]} milhar(es)')
    print(f'Esse número possui {numero[1]} centena(s)')
    print(f'Esse número possui {numero[2]} dezena(s)')
    print(f'Esse número possui {numero[3]} unidade(s)')
elif numero < 100:
    numero = "00" + str(numero)
    print(f'Esse número possui {numero[0]} milhar(es)')
    print(f'Esse número possui {numero[1]} centena(s)')
    print(f'Esse número possui {numero[2]} dezena(s)')
    print(f'Esse número possui {numero[3]} unidade(s)')
elif numero < 1000:
    numero = "0" + str(numero)
    print(f'Esse número possui {numero[0]} milhar(es)')
    print(f'Esse número possui {numero[1]} centena(s)')
    print(f'Esse número possui {numero[2]} dezena(s)')
    print(f'Esse número possui {numero[3]} unidade(s)')
else:
    numero = str(numero)
    print(f'Esse número possui {numero[0]} milhar(es)')
    print(f'Esse número possui {numero[1]} centena(s)')
    print(f'Esse número possui {numero[2]} dezena(s)')
    print(f'Esse número possui {numero[3]} unidade(s)')
