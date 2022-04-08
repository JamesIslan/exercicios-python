usuario = int()
numeros = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    usuario = int(input('Digite aqui um número entre 0 e 20: '))
    if 0 <= usuario <= 20:
        print(f'{usuario} por extenso é {numeros[usuario]}')
        continue
    else:
        print('Digite um número válido')
        continue