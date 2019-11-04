class ParseRequest(str):
    def parse_url(self):
        lines = self.splitlines()
        url = lines[0].split()[1]
        position = url.find("://")
        if position != -1:
            url = url[(position + 3):]
        return url

    def parse_data(self):
        #понять как вытащить данные
        return

    def parse_host_port(self):
        #понять как вытащить порт и хост
        host, port = 1, 2
        return host, port

    @staticmethod
    def create_config(host, port, data):
        dictionary = {
            "host": host,
            "port": port,
            "data": data
        }
        return dictionary
