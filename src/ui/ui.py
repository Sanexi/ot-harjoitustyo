from tkinter import Tk, ttk, constants, StringVar, IntVar
from converter.converter import Converter, ExchangeRateApi


class UI:
    def __init__(self, root):
        self._root = root
        self._amount = IntVar()
        self._ran = False

        self.default_from_curr = StringVar()
        self.default_from_curr.set("EUR")
        self.default_to_curr = StringVar()
        self.default_to_curr.set("USD")

        self.converter = Converter(ExchangeRateApi())
        self.currencies = self.converter.currencies

    def start(self):
        self._from_curr_menu = ttk.Combobox(
            master=self._root, textvariable=self.default_from_curr, values=self.currencies)
        self._to_curr_menu = ttk.Combobox(
            master=self._root, textvariable=self.default_to_curr, values=self.currencies)
        self._amount = ttk.Entry(master=self._root)
        self._convert_button = ttk.Button(
            master=self._root, text="Convert", command=self._run_convert)

        self._from_curr_menu.grid(
            row=0, column=0, sticky=(constants.W), padx=10, pady=10)
        self._to_curr_menu.grid(row=0, column=1, sticky=(
            constants.E), padx=10, pady=10)
        self._amount.grid(row=1, column=0, columnspan=2, pady=10)
        self._convert_button.grid(row=2, column=0, columnspan=2, pady=10)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

    def _run_convert(self):
        count = self._amount.get()
        from_curr = self._from_curr_menu.get()
        to_curr = self._to_curr_menu.get()
        result = self.converter.convert(count, from_curr, to_curr)
        output = f"{count} {from_curr} = {result} {to_curr}"
        date = f"as of {self.converter.date()}"

        if self._ran:
            self.result_label.destroy()
            self.date_label.destroy()
        self._ran = True

        self.result_label = ttk.Label(master=self._root, text=output)
        self.date_label = ttk.Label(master=self._root, text=date)

        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)
        self.date_label.grid(row=4, column=0, columnspan=2, pady=10)
