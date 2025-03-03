import socket
import logging


class HttpsWorker:
    logging.basicConfig(filename="logs.log", filemode="w", level=logging.INFO, format='%(asctime)s - %(message)s',
                        datefmt='%d-%b-%y %H:%M:%S')

    @staticmethod
    def create_connection_connect(client, config, dict_sockets_connection, actual_socket):
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            logging.info("Инициализируем сокет для https: {0}".format(server))
            server.connect((config["host"], config["port"]))
            logging.info("Подключаемся к {0}, через порт {1}".format(config["host"], config["port"]))
            server.settimeout(0.1)
            client.send(b"HTTP/1.1 200 Connection established\nProxy-Agent: THE BB Proxy\n\n")
            HttpsWorker.refresh_collections_socket(dict_sockets_connection, actual_socket, client, server)
        except Exception as e:
            print(e)

    @staticmethod
    def refresh_collections_socket(dict_sockets_connection, actual_socket, client, server):
        dict_sockets_connection[client] = server
        dict_sockets_connection[server] = client
        actual_socket.add(client)
        actual_socket.add(server)



