import select
import socket
import sys
import logging
from work_with_data import DataParser, DataReceiver
from work_with_http import HttpWorker
from work_with_https import HttpsWorker

logging.basicConfig(filename="logs.log", filemode="w", level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


def process_request(sock, data, dict_sockets_connection, actual_socket):
    config = DataParser.create_config(data)
    logging.info("Парсим данные и создаем соединение")
    if len(data) == 0 or len(config) == 0:
        return
    logging.info("Конфиг с данными: {0}".format(config))
    if config["method"] == b'GET':
        HttpWorker.create_connection_get(sock, config)
        sock.close()
    if config["method"] == b'CONNECT':
        HttpsWorker.create_connection_connect(sock, config, dict_sockets_connection, actual_socket)


def main():
    dict_sockets_connections = {}
    actual_socket = set()
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 8080))
        logging.info("Биндим слушающий сокет на порт 8080")
        s.listen(100)
        actual_socket.add(s)
    except Exception as e:
        print(e)
        sys.exit(1)
    while True:
        try:
            act_soc, _, _ = select.select(actual_socket, [], [])
            for sock in act_soc:
                if sock == s:
                    client, addr = s.accept()
                    logging.info("Получаем данные от {0}".format(socket.socket.getsockname(client)))
                    data = DataReceiver.receive_data(client)
                    process_request(client, data, dict_sockets_connections, actual_socket)
                else:
                    logging.info("Получаем данные от {0}".format(socket.socket.getsockname(sock)))
                    data = DataReceiver.receive_data(sock)
                    logging.info("Отправляем данные {0}".format(socket.socket.getsockname(dict_sockets_connections[sock])))
                    dict_sockets_connections[sock].send(data)
        except Exception as e:
            sys.exit(e)



if __name__ == '__main__':
    main()
