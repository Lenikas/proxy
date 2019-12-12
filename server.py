import socket
from parser_data import ParserData
import logging


class Server:
    logging.basicConfig(filename="logs.log", filemode="w", level=logging.DEBUG)

    @staticmethod
    def create_connection_get(client, config):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            logging.info("Инициализируем сервер")
            server.connect((config["host"], config["port"]))
            server.send(config["data"])
            reply = server.recv(8192)
            server.settimeout(0.2)
            while len(reply):
                try:
                    client.send(reply)
                    reply = server.recv(8192)
                except socket.timeout:
                    break
            logging.info("Ответ сервера: {0}".format(reply))
            server.close()
            client.close()
        except Exception as e:
            print(e)
            server.close()
            client.close()
            return

    # @staticmethod
    # def create_connection_connect(client, config):
    #     server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     server.connect((config["host"], config["port"]))
    #     server.settimeout(0.3)

    @staticmethod
    def process_request(sock, data):
        logging.info("Парсим данные и создаем соединение")
        if not data:
            return
        config = ParserData.create_config(data)
        logging.info("Конфиг с данными: {0}".format(config))
        if config["method"] == b'GET':
            Server.create_connection_get(sock, config)
            sock.close()
        # if config["method"] == b'CONNECT':
        #     Server.create_connection_connect(sock, config)

