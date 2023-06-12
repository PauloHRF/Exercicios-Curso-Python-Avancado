# Usando docstrings para documentar métodos

#Primeira linha é reservada para explicar a função
#Params:
    #Próximas linhas devem evidenciar os argumentos que a função utiliza
    #Caso haja algum valor padrão este deve ser representado
#Return:
    #Última linha apresenta o que será retornado.
#Caso não hajam paramêtros ou argumentos estas linhas devem ser omitidas.

def quadrado(a):
    '''Função que gera o quadrado de um número.
    
    Params:
        a: Primeiro argumento. Um número real

    Return:
        b: O quadrado do argumento recebido.
    '''
    b = a^2
    return b

# Podemos utilizar a função dunder __doc__ para verificar a docstring
def main():
    print(quadrado.__doc__)
    
    # As funções do python tambem possuem docstrings que podemos consultar.
    print(print.__doc__)





if __name__ == "__main__":
    main()
