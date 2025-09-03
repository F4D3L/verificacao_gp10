def sao_anagramas(string1, string2):
    palavra_teste = string2[::-1]
    if palavra_teste == string1:
        return True
    else:
        return False
    
def cifra_de_cesar(texto, deslocamento):
    # TODO: Implementar lógica
    pass

def encontrar_maior_palavra(frase):
    # TODO: Implementar lógica
    pass


print(sao_anagramas("roma", "amor"))
print(sao_anagramas("casa", "arroz"))