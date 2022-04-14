carteira = "{:.2f}".format(
    float(input('Digite aqui a quantia em Reais (R$): ')))
print(
    f'O valor de {"R$" + carteira} equivale a {"US$" + "{:.2f}".format(float(carteira) / float(5.54))}')
