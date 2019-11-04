from my_parser import ParseRequest
from server import Server


def process_request(client, request):
    host, port = ParseRequest.parse_host_port(request)
    data = ParseRequest.parse_data(request)
    config = ParseRequest.create_config(host, port, data)
    Server.create_connection(client, config)
    client.close()


def main():
    return


if __name__ == '__main__':
    main()
