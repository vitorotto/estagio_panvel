def animais (posicao_bob, posicao_rex, posicao_oli):

    dist_bob_gato = abs(posicao_bob - posicao_oli)
    dist_rex_gato = abs(posicao_rex - posicao_oli)

    if dist_bob_gato < dist_rex_gato:
        return "Bob"
    else:
        if dist_rex_gato < dist_bob_gato:
            return "Rex"
        else:
            return "Oli"
        
posicao_bob = float(input("Qual a distancia de Bob em relacao ao gato? "))
posicao_rex = float(input("Qual a distancia de Rex em relacao ao gato? "))
posicao_oli = 0

vencedor = animais(posicao_bob, posicao_rex, posicao_oli)
print("O vencedor é: %s" %vencedor)


        
