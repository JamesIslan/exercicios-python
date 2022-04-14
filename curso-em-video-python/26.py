frase = input('Digite aqui uma frase qualquer: ').lower()
if 'a' in frase:
    print(f'A letra "A" aparece {frase.count("a")} vezes na sua frase')
    primeira_ocorrencia = int(frase.index("a"))
    print(
        f'A letra "A" aparece pela primeira vez na posição {primeira_ocorrencia}')
    print(
        f'A letra "A" aparece pela última vez na posição {len(frase) - 1 - frase[::-1].index("a")}')
