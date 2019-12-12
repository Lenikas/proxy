import socket
import sys
from server import Server
import logging

logging.basicConfig(filename="logs.log", filemode="w", level=logging.DEBUG)


def receive_data(client):
    logging.info("Получаем данные клиента")
    client.settimeout(1)
    data = b''
    try:
        part = client.recv(8192)
        while part:
            data += part
            part = client.recv(8192)
    finally:
        logging.info("Полученные данные: {0}".format(data))
        return data


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", 8080))
        s.listen(100)
    except Exception as e:
        print(e)
        sys.exit(1)
    while True:
        try:
            client, address = s.accept()
            data = receive_data(client)
            Server.process_request(client, data)
        except Exception as e:
            print(e)
            client.close()
            break



if __name__ == '__main__':
    main()
