# define enumerations using the Enum base class
from enum import Enum,auto

# TODO: Defina a classe Fruta que herda de Enum
class Fruta(Enum):
    UVA = 1
    MAÇA = 3
    PERA = 2
    GOIABA = 5
    MORANGO = auto()

def main():
    # TODO: Objetos enum possuem valores e tipos de fácil leitura
    # pode ser visualizado com print e com repr de forma mais detalhada
    print(Fruta.UVA)
    print(type(Fruta.UVA))
    print(repr(Fruta.UVA))

    # TODO: Objetos enum possuem propriedades "name" (nome) e
    # "value" (valor)
    # .name .value para acessar respectivamente nome e valor
    print(Fruta.UVA.name, Fruta.UVA.value)


    # TODO: Mostre o valor gerado automaticamente para MORANGO)
    # ele receberá o valor max+1
    print(Fruta.MORANGO.value)

    # TODO: É possível usar objetos enum como chaves
    minhas_frutas = {}
    minhas_frutas[Fruta.MAÇA] = "Fruta vermelha"
    print(minhas_frutas[Fruta.MAÇA])


if __name__ == "__main__":
    main()
