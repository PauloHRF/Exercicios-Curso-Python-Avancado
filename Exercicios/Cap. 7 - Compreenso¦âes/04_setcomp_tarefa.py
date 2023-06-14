# Usando set comprehensions


def main():
    # Definindo uma lista de temperaturas
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # TODO: Crie um set com as temperaturas em Fahrenheit
    # Dica: Fórmula pra converter para Fahrenheit -> (t * 9/5) + 32
    ftemps_set = {(t * 9/5) + 32 for t in ctemps}
    print(ftemps_set)


    # TODO: Crie um set a partir de uma string
    texto = "abcdefgh"
    letras = {c for c in texto if not c.isspace()}
    print(letras)



if __name__ == "__main__":
    main()
