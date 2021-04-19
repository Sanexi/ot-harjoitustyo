from tkinter import Tk
import unittest
from ui import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        window = Tk()
        self.ui = UI(window)

    def test_correct_default_from_curr(self):
        from_curr = self.ui.default_from_curr.get()
        self.assertEqual(from_curr, "EUR")
    
    def test_correct_default_to_curr(self):
        to_curr = self.ui.default_to_curr.get()
        self.assertEqual(to_curr, "USD")