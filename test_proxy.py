import unittest
from parser_data import ParserData


class TestProxy(unittest.TestCase):
    with open("test_data.txt", "rb") as file:
        data = file.read()

    def test_parse_method(self):
        method = ParserData.parse_method(TestProxy.data)
        expected = b'GET'
        self.assertEqual(expected, method)

    def test_parse_host(self):
        host = ParserData.parse_host_get(TestProxy.data)
        expected = b'fanserials.haus'
        self.assertEqual(expected, host)

    def test_parse_port_get(self):
        port = ParserData.parse_server_port_get(TestProxy.data)
        expected = 80
        self.assertEqual(expected, port)

    def test_create_config_get(self):
        config = ParserData.create_config(TestProxy.data)
        expected = {
            "port": 80,
            "host": b'fanserials.haus',
            "method": b'GET',
            "data": TestProxy.data
        }
        self.assertDictEqual(expected, config)

