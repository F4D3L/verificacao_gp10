def sao_anagramas(string1, string2):
    # TODO: Implementar lógica
    pass

def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar lógica
    pass

def encontrar_maior_palavra(frase):
    # Separa a frase em palavras e remove pontos e vírgulas
    palavras = [i.strip(".,!?") for i in frase.split()]
    
    maior = ""
    for i in palavras:
        if len(i) > len(maior):
            maior = i
    return maior


frase = "qual é a maiorpalavra!?!?!?"
print(encontrar_maior_palavra(frase))
