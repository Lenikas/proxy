import unittest
from work_with_data import DataParser


class TestProxy(unittest.TestCase):
    with open("test_data.txt", "rb") as file:
        data = file.read()

    def test_parse_method(self):
        method = DataParser.parse_method(TestProxy.data)
        expected = b'GET'
        self.assertEqual(expected, method)

    def test_parse_host(self):
        host = DataParser.parse_host_get(TestProxy.data)
        expected = b'fanserials.haus'
        self.assertEqual(expected, host)

    def test_parse_port_get(self):
        port = DataParser.parse_server_port_get(TestProxy.data)
        expected = 80
        self.assertEqual(expected, port)

    def test_create_config_get(self):
        config = DataParser.create_config(TestProxy.data)
        expected = {
            "port": 80,
            "host": b'fanserials.haus',
            "method": b'GET',
            "data": TestProxy.data
        }
        self.assertDictEqual(expected, config)

