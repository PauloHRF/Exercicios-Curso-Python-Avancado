# Usando objetos OrderedDict
from collections import OrderedDict


def main():
    # Lista de times com número de partidas ganhas e perdidas
    times_fut = [("Cruzeiro", (18, 12)), ("Vasco", (24, 6)), 
                 ("Avaí", (20, 10)), ("Flamengo", (22, 8)),
                 ("Palmeiras", (15, 15)), ("Santos", (20, 10)), 
                 ("Botafogo", (16, 14)), ("Fluminense", (25, 5))]

    # Ordenando os times pela quantidade de vitórias
    times_ord = sorted(times_fut, key=lambda t: t[1][0], reverse=True)

    # TODO: Crie um dicionário ordenado com os times
    # O dicionario ordenado se lembra da ordem que os valores foram 
    # inseridos, inserindo a lista ordenada obtemos um dicionario
    # ordenado com os times mais vitoriosos 
    futOrdered = OrderedDict(times_ord)
    print(futOrdered)

    # TODO: Use popitem para remover o item do topo
    # popitem passa os valores para as variaveis fornecidas
    # passando o valor false ele organiza no modo FIFO
    nome, estatistica = futOrdered.popitem(False)
    print(nome, estatistica)

    # TODO: Faça um teste de igualdade
    # O dicionário não é compreendido como o mesmo pois a ordem é diferente
    a = OrderedDict({"a": 2, "b": 3, "c": 1})
    b = OrderedDict({"c": 1, "b": 3, "a": 2})
    print(a == b)

if __name__ == "__main__":
    main()
