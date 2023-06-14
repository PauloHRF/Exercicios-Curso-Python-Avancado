# Personalizando o retorno do logging
import logging


#criando dados para serem utuilizados pelo log
dados={'nome': 'João'}

# TODO: Crie uma outra função para rodar o log
# configurando log em uma função
def log():
    logging.debug('Mensagem padrão de LOG', extra=dados)

def main():
    # TODO: Defina o nível de log para debug e um arquivo para salvar
    # o retorno. Use também uma formatação personalizada
    # configurado formatação personalizada para as mensagens de log

    formato = ("%(asctime)s: %(levelname)s: %(funcName)s "
               "Linha:%(lineno)d Nome:%(nome)s %(message)s")

    logging.basicConfig(filename="output1.log",
                        level=logging.DEBUG,
                        format=formato)

    # as chamadas de log devem receber os dados atráves do parametro extra
    logging.info("Esta é uma mensagem de informação", extra=dados)
    logging.warning("Esta é uma mensagem de aviso", extra=dados)
    log()

if __name__ == "__main__":
    main()
