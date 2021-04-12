import unittest
from converter import Converter
from datetime import datetime
import requests

class TestConverter(unittest.TestCase):
    def setUp(self):
        pass

    def test_correct_date(self):
        converter = Converter()
        converter_date = converter.date()
        now = datetime.now()
        now = now.strftime("%d.%m.%Y")
        self.assertEqual(converter_date, now)
    
    def test_convert_success(self):
        converter = Converter()
        self.assertEqual(converter.success, True)
