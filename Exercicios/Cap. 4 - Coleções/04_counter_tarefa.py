# Usando a classe Counter
from collections import Counter


def main():
    # Uma lista de estudantes na turma A
    turma_a = ["Bárbara", "João", "Carlos", "Dário", "Priscila", "Ana",
               "Kevin", "João", "Marina", "Bianca", "Gustavo",
               "Fernanda"]

    # Uma lista de estudantes na turma B
    turma_b = ["Hiro", "Bruno", "Claudia", "Débora", "Fernanda",
               "Gabriela", "Leticia", "João", "Jairo", "Samuel",
               "Taciana", "Gabriel"]

    # TODO: Crie um Counter para as turmas A e B
    # O modulo counter organiza a lista como um dicionario, 
    # tendo as entidades como chaves e a inicdências como valores
    turmaA=Counter(turma_a)
    turmaB=Counter(turma_b)


    # TODO: Quantos estudantes na turma A se chamam João?
    # Chamando o nome da chave recebemos de volta o valor
    print('Incidencias do nome João:', turmaA['João'])

    # TODO: Quantos estudantes estão na turma A?
    # O metodos values seleciona apenas os valores do counter,
    # assim facilitando a soma.
    print(sum(turmaA.values()))

    # TODO: Combine as duas turmas
    # Unimos as turmas
    turmaA.update(turmaB)
    print(turmaA)

    # TODO: Quais os 3 nomes mais comuns nas duas turmas?
    # Metodo most_common, podemos selecionar o top x do counter.
    print(turmaA.most_common(3))

    # TODO: Separe as duas turmas e mostre o nome mais comum da turma a
    turmaA.subtract(turmaB)
    print(turmaA.most_common(1))

    # TODO: Qual a intersecção de nomes entre as duas turmas?
    print(turmaA & turmaB)

if __name__ == "__main__":
    main()
