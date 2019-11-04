import socket


class Server:
    @staticmethod
    def create_connection(client, config):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((config["host"], config["port"]))
        server.send(config["data"])
        reply = server.recv(8192)
        while len(reply) != 0:
            try:
                client.send(reply)
                reply = server.recv(8192)
            except socket.error:
                break
        server.close()
        client.close()
        return



