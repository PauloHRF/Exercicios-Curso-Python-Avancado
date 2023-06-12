# Iteradores do módulo itertools
import itertools


def condicao(x):
    if x < 40:
        return True


def main():
    # TODO: Iterador cycle pode ser usado como o iter para iterar sobre
    # uma lista
    pessoas = ["Jessica", "Leticia", "Gustavo"]
    ciclo = itertools.cycle(pessoas)
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))
    print(next(ciclo))

    # TODO: Use count para criar um contador
    contador = itertools.count(100, 10)
    print(next(contador))
    print(next(contador))
    print(next(contador))

    # TODO: A função accumulate cria um iterdor que acumula valores
    valores = [10, 20, 30, 40, 50, 40, 30]
    a = list(itertools.accumulate(valores))
    print(a)

    # TODO: Use a função chain para conectar listas
    valores_2 = [50, 30, 20, 10, 70]
    b = list(itertools.chain(valores,valores_2))
    print(b)

    # TODO: As funções dropwhile e takewhile vai retornar valores até
    # que uma condição seja atingida
    print(list(itertools.dropwhile(condicao,b)))
    print(list(itertools.takewhile(condicao,b)))


if __name__ == "__main__":
    main()
