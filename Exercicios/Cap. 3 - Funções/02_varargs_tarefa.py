# Uso de argumentos variáveis


# TODO: Defina uma função que recebe argumentos variáveis
# O sinal de estrela define que o argumento é variavel
# O nome args é uma boa prática,
# para identificarmos facilmente o argumento variavel.
def adicao(*args):
    return sum(args)


def main():
    # TODO: Passe argumentos diferentes para o método adicao()
    # A função recebe os argumentos em forma de tupla
    # E os utiliza de acordo, sem quantidades fixas.

    print(adicao(45,21,65,44,2))
    print(adicao(2,12,54))

    # TODO: Passe uma lista para o método adicao()
    # Neste caso precisamos passar o sinal da estrela 
    # para desempacotar a lista.
    valores = [4,1,84,6]
    print(adicao(*valores))

if __name__ == "__main__":
    main()
