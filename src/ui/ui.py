from tkinter import Tk, ttk, constants, StringVar, IntVar, messagebox, font
from PIL import Image, ImageTk
from converter.converter import Converter, ExchangeRateApi


class UI:
    def __init__(self, root):
        self._root = root
        self._amount = IntVar()
        self._ran = False

        self._root.bind('<Return>', self._run_convert)

        self.default_from_curr = StringVar()
        self.default_from_curr.set("EUR")
        self.default_to_curr = StringVar()
        self.default_to_curr.set("USD")

        self.font_style = font.Font(family="Futura", size=10)
        self.style = ttk.Style()
        self.style.configure('TButton', font=self.font_style)

        self.converter = Converter(ExchangeRateApi())
        self.currencies = self.converter.currencies

    def start(self):
        image = Image.open("./src/images/background.jpg")
        self.background = ImageTk.PhotoImage(image)
        self.background_label = ttk.Label(
            master=self._root, image=self.background)

        self._from_curr_menu = ttk.Combobox(
            master=self._root, textvariable=self.default_from_curr, values=self.currencies)
        self._to_curr_menu = ttk.Combobox(
            master=self._root, textvariable=self.default_to_curr, values=self.currencies)
        self._swap_currencies_button = ttk.Button(
            master=self._root, text="<>", command=self._swap_currencies)
        self._amount = ttk.Entry(master=self._root)
        self._convert_button = ttk.Button(
            master=self._root, text="Convert", command=self._run_convert)

        self._from_curr_menu.configure(font=self.font_style)
        self._to_curr_menu.configure(font=self.font_style)
        self._swap_currencies_button.configure(style="TButton")
        self._convert_button.configure(style="TButton")

        self.background_label.place(x=0, y=0)
        self._from_curr_menu.grid(
            row=0, column=0, sticky=(constants.W), padx=20, pady=20)
        self._swap_currencies_button.grid(row=0, column=1, padx=20, pady=20)
        self._to_curr_menu.grid(row=0, column=2, sticky=(
            constants.E), padx=20, pady=20)
        self._amount.grid(row=1, column=1, pady=20)
        self._convert_button.grid(row=2, column=1, pady=20)

        self._root.grid_columnconfigure(1, weight=1, minsize=300)

    def _run_convert(self, event=None):
        count = self._amount.get()
        from_curr = self._from_curr_menu.get()
        to_curr = self._to_curr_menu.get()

        try:
            count = float(count)
        except:
            messagebox.showinfo(
                "Error", "Wrong input, format input like this: 12.5 (not 12,5 €)")
            return

        self.result = self.converter.convert(count, from_curr, to_curr)
        output = f"{self.result} {to_curr}"
        date = f"as of {self.converter.date()}"

        if self._ran:
            self.result_label.destroy()
            self.date_label.destroy()
        self._ran = True

        self.result_label = ttk.Label(master=self._root, text=output)
        self.date_label = ttk.Label(master=self._root, text=date)
        self.copy_button = ttk.Button(
            master=self._root, text="Copy", command=self._copy_to_clipboard)

        self.result_label.configure(font=self.font_style)
        self.date_label.configure(font=self.font_style)
        self.copy_button.configure(style="TButton")

        self.result_label.grid(row=3, column=1, pady=20)
        self.date_label.grid(row=4, column=1)
        self.copy_button.grid(row=5, column=1, pady=20)

    def _copy_to_clipboard(self):
        self._root.clipboard_clear()
        self._root.clipboard_append(self.result)
        messagebox.showinfo("", "Copied to clipboard!")

    def _swap_currencies(self):
        current_from = self._from_curr_menu.get()
        current_to = self._to_curr_menu.get()
        self.new_from = StringVar()
        self.new_from.set(current_to)
        self.new_to = StringVar()
        self.new_to.set(current_from)

        self._from_curr_menu.destroy()
        self._to_curr_menu.destroy()

        self._from_curr_menu = ttk.Combobox(
            master=self._root, textvariable=self.new_from, values=self.currencies)
        self._to_curr_menu = ttk.Combobox(
            master=self._root, textvariable=self.new_to, values=self.currencies)

        self._from_curr_menu.configure(font=self.font_style)
        self._to_curr_menu.configure(font=self.font_style)

        self._from_curr_menu.grid(
            row=0, column=0, sticky=(constants.W), padx=20, pady=20)
        self._to_curr_menu.grid(row=0, column=3, sticky=(
            constants.E), padx=20, pady=20)
