from datetime import datetime
import unittest
import requests
from converter.converter import Converter, ExchangeRateApi


class StubExchangeRateApi:
    def __init__(self, url):
        self._url = url

    def get_rates(self):
        response = requests.get(self._url)
        return response.json()


class TestConverter(unittest.TestCase):
    def setUp(self):
        pass

    def test_correct_date(self):
        converter = Converter(ExchangeRateApi())
        converter_date = converter.date()
        now = datetime.now()
        now = now.strftime("%d.%m.%Y")
        self.assertEqual(converter_date, now)

    def test_convert_success(self):
        converter = Converter(ExchangeRateApi())
        self.assertEqual(converter.success, True)

    def test_exchange_rates(self):
        converter = ExchangeRateApi().get_rates()
        url = "https://api.exchangerate.host/latest"
        test_exchange_rates = StubExchangeRateApi(url)
        stub = test_exchange_rates.get_rates()
        self.assertEqual(converter["rates"], stub["rates"])

    def test_failed_conversion(self):
        converter = Converter(ExchangeRateApi())
        result = converter.convert("", "USD", "EUR")
        self.assertEqual(result, False)

    def test_conversion(self):
        converter = Converter(ExchangeRateApi())
        result = float(converter.convert(1, "EUR", "USD"))
        url = "https://api.exchangerate.host/latest"
        test_exchange_rates = StubExchangeRateApi(url)
        stub = test_exchange_rates.get_rates()
        self.assertAlmostEqual(result, float(stub["rates"]["USD"]), 4)
