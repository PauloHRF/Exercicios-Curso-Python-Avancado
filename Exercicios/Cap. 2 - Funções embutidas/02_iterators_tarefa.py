# Usando funções iteradoras como enumerate, zip, iter, next


def main():
    # Defina a lista de dias da semana em Português e English
    dias = ["Dom", "Seg", "Ter", "Qua", "Qui", "Sex", "Sab"]
    dias_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    # TODO: Use a função iter para criar um iterador sobre uma lista
    iterador = iter(dias)
    print(next(iterador))


    # TODO: Use uma função para iterar sobre um arquivo
    with open("dados.txt", 'r') as fp:
        for linha in iter(fp.readline, ''):
            print(linha)

    # TODO: Use a iteração tradicional (range) sobre a lista dias
    for i in range(len(dias)):
        print(dias[i])



    # TODO: Usar a função enumerate reduz a quantidade de código e te
    # dá um contador
    a = list(enumerate(dias))
    for i in range(len(dias)):
        print(a[i])


    # TODO: Use a função zip para combinar as listas
    for i in zip(dias,dias_en):
        print(i)

    # TODO: Combine zip com enumerate para formatar o resultado
    for i, m in enumerate(zip(dias,dias_en)):
        print('index:', i, 'Dia: ', m[0], 'Day: ', m[1])

if __name__ == "__main__":
    main()
