# Vitor Hugo Otto

def criptografar(texto, rotacoes): # Função para criptografar a String
    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    texto_criptografado = ""

    for letra in texto:
        if letra.lower() in alfabeto:
            indice = (alfabeto.index(letra.lower()) + rotacoes) % len(alfabeto)
            letra_criptografada = alfabeto[indice]
            if letra.isupper():
                texto_criptografado += letra_criptografada.upper()
            else:
                texto_criptografado += letra_criptografada
        else:
            texto_criptografado += letra

    return texto_criptografado

def descriptografar(texto_criptografado, rotacoes): # Função para criptografar a String
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    texto_descriptografado = ""

    for letra in texto_criptografado:
        if letra.lower() in alfabeto:
            indice = (alfabeto.index(letra.lower()) - rotacoes) % len(alfabeto)
            letra_descriptografada = alfabeto[indice]
            if letra.isupper():
                texto_descriptografado += letra_descriptografada.upper()
            else:
                texto_descriptografado += letra_descriptografada
        else:
            texto_descriptografado += letra

    return texto_descriptografado

texto_original = input("Insira o texto que deseja criptografar: ")
rotacoes = int(input("Quantas rotacoes deseja efetuar? "))

texto_criptografado = criptografar(texto_original, rotacoes)
print("Texto Criptografado:", texto_criptografado)

texto_descriptografado = descriptografar(texto_criptografado, rotacoes)
print("Texto Descriptografado:", texto_descriptografado)
