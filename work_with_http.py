import socket
import sys
import logging


class HttpWorker:

    logging.basicConfig(filename="logs.log", filemode="w", level=logging.INFO, format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    @staticmethod
    def create_connection_get(client, config):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        logging.info("Инициализируем сокет для http: {0}".format(server))
        try:
            server.connect((config["host"], config["port"]))
            logging.info("Подключаемся к {0}, через порт {1}".format(config["host"], config["port"]))
            server.send(config["data"])
            reply = server.recv(8192)
            server.settimeout(0.2)
            while len(reply):
                try:
                    logging.info("Получаем данные с сервера и отправляем клиенту: {0}".format(reply))
                    client.send(reply)
                    reply = server.recv(8192)
                except socket.timeout:
                    break
            logging.info("Закрываем соединение между {0} и {1}".format(socket.socket.getsockname(server),
                                                                       socket.socket.getsockname(client)))
            server.close()
            client.close()
        except Exception as e:
            server.close()
            client.close()
            sys.exit(e)