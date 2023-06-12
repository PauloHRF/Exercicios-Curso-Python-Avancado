# Usando funções transformadoras: sorted, filter, map


def primeiro_filtro(x):
    if x%2 ==0:
        return False
    else: return True


def segundo_filtro(x):
    if x.islower():
        return False
    else: return True


def quadrado(x):
    return x**2


def nota_para_conceito(x):
    if x >= 9:
        return 'A'
    elif 7.5 <= x < 9:
        return 'B'
    elif 5.5 <= x < 7.5:
        return 'C'
    elif 5 <= x < 5.5:
        return 'D'
    else:
        return 'F'


def main():
    # Definindo sequencias para usarmos nesta tarefa
    numeros = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    letras = "abcDeFGHiJklmnoP"
    notas = (4.5, 8.9, 9.4, 7.8, 6.1, 5.3, 9.9, 3.4)

    # TODO: Use filter para remover itens de uma lista
    a = list(filter(primeiro_filtro, numeros))
    print(a)


    # TODO: Use filter numa sequência de caracteres
    b = list(filter(segundo_filtro, letras))
    print(b)

    # TODO: Use map para criar uma nova sequência de valores
    c = list(map(quadrado,numeros))
    print(c)

    # TODO: Use sorted e map para mudar as noas para conceito
    d = list(map(nota_para_conceito,sorted(notas)))
    print(d)

if __name__ == "__main__":
    main()
