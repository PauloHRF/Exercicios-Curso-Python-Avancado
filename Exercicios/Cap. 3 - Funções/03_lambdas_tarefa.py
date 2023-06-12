# Usando lambdas como funções de uma linha


def celsius_para_fahrenheit(temp):
    return (temp * 9/5) + 32


def fahrenheit_para_celsius(temp):
    return (temp-32) * 5/9


def main():
    temp_em_c = [0, 12, 34, 100]
    temp_em_f = [32, 65, 100, 212]

    # TODO: Defina funções tradicionais para converter as temperaturas
    for i in temp_em_c:
        print('Temperatura em fahrenheit:', celsius_para_fahrenheit(i))

    for i in temp_em_f:    
        print('Temperatura em celsius:', fahrenheit_para_celsius(i))

    # TODO: Use lambdas tpara converter as temperaturas
    # Funções possuem a estrutura lambda argumentos : função
    # Neste exemplo utilizamos a função map para passar os valores à lambda
    # E posteriormente list para deixar nosso map legivel.
    print(list(map(lambda i : (i * 9/5) + 32, temp_em_c)))
    print(list(map(lambda i : (i-32) * 5/9, temp_em_f)))




if __name__ == "__main__":
    main()
