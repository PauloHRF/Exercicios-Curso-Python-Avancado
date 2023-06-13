# Deques são filas duplamente terminadas
import collections
import string


def main():
    # TODO: Inicialize um deque com letras minúsculas
    dq = collections.deque('adsgvkoasd')

    # TODO: Deques suportam o método len(), mostre o tamanho da deque
    print(len(dq))

    # TODO: Itere sobre a deque criada
    for i in dq:
        print(i, end=", ")

    # TODO: Manipule os itens em qualquer um dos terminais
    # comandos pop e append padrões operam pela direita
    # mas podemos utilizar popleft e appendleft para operar pela esquerda
    dq.pop()
    dq.popleft()
    dq.append("C")
    dq.appendleft("C")
    print("\n",dq)

    # TODO: Rotacione a deque
    # podemos rotacionar todos os elementos do deque com o metodo rotate
    dq.rotate(5)
    print(dq)

if __name__ == "__main__":
    main()
