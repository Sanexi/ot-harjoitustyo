from tkinter import Tk, ttk, constants, StringVar
from converter.converter import Converter, ExchangeRateApi

class UI:
    def __init__(self, root):
        self._root = root
        self._amount = None

        self.default_from_curr = StringVar()
        self.default_from_curr.set("EUR")
        self.default_to_curr = StringVar()
        self.default_to_curr.set("USD")

        self.converter = Converter(ExchangeRateApi())
        self.currencies = self.converter.currencies

    def start(self):
        self._from_curr_menu = ttk.Combobox(self._root, textvariable=self.default_from_curr, values=self.currencies)
        self._to_curr_menu = ttk.Combobox(self._root, textvariable=self.default_to_curr, values=self.currencies)
        self._amount = ttk.Entry(master=self._root)
        convert_button = ttk.Button(master=self._root, text="Convert", command=self.convert())


        self.from_curr_menu.grid(row=0, column=0)
        self.to_curr_menu.grid(row=0, column=1)
        self._amount.grid(row=1, column=0)
        convert_button.grid(row=2, column=0)

    def convert(self):
        count = self._amount.get()
        from_curr = self._from_curr_menu.get()
        to_curr= self._to_curr_menu.get()
        print(self.converter.convert(count, from_curr, to_curr))



window = Tk()
window.title("Currency Converter")

ui = UI(window)
ui.start()

window.mainloop()