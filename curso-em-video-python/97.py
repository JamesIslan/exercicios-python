# Tratamento de erro incluso
def escrever(msg: str):
    print('~' * (len(msg) + 6))
    print(f'   {msg}   ')
    print('~' * (len(msg) + 6))


escrever('Me siga no Github — github.com/jamesislan')

mensagem = str(input('Digite a mensagem a ser exibida: '))

escrever(mensagem)
