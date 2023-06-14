# Uso do módulo logging

# TODO: Use o módulo embutido logging
from datetime import date
import logging

def main():
    # TODO: Use basicConfig para configurar seu logging
    # Configuramos o log no modo escrita e o nome do arquivo gerado
    logging.basicConfig(level=logging.DEBUG,
                        filemode='w',
                        filename='output.log')

    # Testando cada um dos níveis de log
    # Cada um deste deve ser utilizado de acordo com a situação
    logging.debug("Esta é uma mensagem de debug")
    logging.info("Esta é uma mensagem de informação")
    logging.warning("Esta é uma mensagem de aviso")
    logging.error("Esta é uma mensagem de erro")
    logging.critical("Esta é uma mensagem crítica")

    # TODO: Use strings para formatar o log
    # Podemos selecionar e registar diversas informações úteis no log
    logging.info("Podemos colocar informações importantes no log,"
                "exemplo: Valor comum: {}, Data do aviso: {}".format(10, date.today()))



if __name__ == "__main__":
    main()
