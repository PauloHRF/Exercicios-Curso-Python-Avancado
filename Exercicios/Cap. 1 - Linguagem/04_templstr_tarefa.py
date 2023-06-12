# Demonstração das funções de string templates
from string import Template

def main():
    # Formatação tradicional usando o método format()
    frase = "Você está assistindo {0} com {1}".format(
        "Python Avançado", "Jessica Temporal")
    print(frase)

    # TODO: Crie um template com placeholders
    # Função Template() recebe uma string com placeholders
    templ = Template("Você está assistindo ${curso} com ${professor}")

    # TODO: Use o método substitute passando argumentos nomeados
    # Substituimos os placeholders de nosso template 
    # com a inserção da estrutura NomeDoPlaceholder = 'ValorDesejado'
    frase_1 = templ.substitute(
        curso='Fundamentos do Big Data: Técnicas e Conceitos',
        professor='Barton Poulson')
    print(frase_1)

    # TODO: Use  o método substitute com um dicionário
    # Podemos criar um dicionario para utilizar no modo substitute,
    # ele deve seguir os nomes do placeholder,
    # elementos extras não afetarão o metodo.
    dict_1 = {
        "curso" : 'Introdução à Amazon Web Services: Computação em Nuvem',
        "professor" : 'Hiroko Nishimura',
        "Data" : '06-06-2023'
    }

    frase_2 = templ.substitute(dict_1)
    print(frase_2)

if __name__ == "__main__":
    main()
