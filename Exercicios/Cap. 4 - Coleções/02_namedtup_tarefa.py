# Uso de objetos namedtuple
import collections


def main():
    # TODO: Crie uma namedtuple para armazenar coordenadas
    # necessitamos importar o modulo collections para usar namedtuples
    # passamos um nome para a tupla e suas chaves
    coordenadas = collections.namedtuple("Coordenadas",['x','y'])

    p1 = coordenadas(15, 20)
    p2 = coordenadas(25, 30)

    print(p1, p2)
    print(p1.x, p2.y)

    # TODO: Use _replace() para criar uma instância nova
    p1 = p1._replace(x=100)
    print(p1)



if __name__ == "__main__":
    main()
