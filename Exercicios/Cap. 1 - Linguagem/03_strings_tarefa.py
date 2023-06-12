# strings e bytes não são diretamente intercambiáveis
# strings contém unicode, bytes são valores de 8 bits

def main():
    # definindo alguns valores iniciais
    a = 'Alfabeto: '
    b = bytes([0x41, 0x42, 0x43, 0x44])

    # TODO: Tente juntar os dois.
    # c = a+b
    # Exception has occurred: TypeError can only concatenate str (not "bytes") to str
    # Recebemos um erro, dizendo que não é possível concatenar strings e bytes.


    # TODO: Bytes e strings precisam ser apropriadamente encoded
    print(a.encode("UTF-8")+b)
    # Recebemos o resultado esperado 'Alfabeto: ABCD'
    # pois strings seguem o padrão UTF-8 


    # TODO: Faça o encode da string como UTF-32
    print(a.encode("UTF-32")+b)
    # Temos sucesso na operção, porém recebemos um código quebrado 
    # \xff\xfe\x00\x00A\x00\x00\x00l\x00\x00\x00f\x00\x00
    # \x00a\x00\x00\x00b\x00\x00\x00e\x00\x00\x00t\x00\x00
    # \x00o\x00\x00\x00:\x00\x00\x00 \x00\x00\x00ABCD
    # devido a mudança de pradrão
    
    # Podemos realizar a operação no sentido contrario e ao inves de
    # transformar a string em bytes podemos transformar os bytes em string
    print(a+b.decode("UTF-8"))


if __name__ == "__main__":
    main()
