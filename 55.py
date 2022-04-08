pesos = list(sorted(map(int, input('Digite aqui os pesos em Kg (separados por espaço): ').split())))
if len(pesos) >5 : print('Digite apenas 5 valores') ; exit()
else : print(f'A pessoa mais magra possui {pesos[0]}Kg') ; print(f'A pessoa mais gorda possui {pesos[-1]}Kg')