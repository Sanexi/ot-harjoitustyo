import requests
from datetime import datetime

class Converter():
    def __init__(self):
        url = "https://api.exchangerate.host/latest"
        response = requests.get(url)
        self.data = response.json()
        self.rates = self.data["rates"]
        self.currencies = list(self.rates.keys())
        self.success = self.data["success"]

    def convert(self, count, a, b):
        if self.success == True:
            if a != "EUR":
                count = count / self.rates[a]
            return f"{self.rates[b]*count:.4f}"

    def date(self):
        date = str(self.data["date"])
        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%d.%m.%Y")
        return date

def main():
    converter = Converter()
    print("Select from following currencies: ")
    print(converter.currencies)
    a = input("Convert from: ")
    count = int(input("Amount: "))
    b = input("Convert to: ")
    print(f"{count} {a} = {converter.convert(count, a, b)} {b} as of {converter.date()}")

if __name__ == "__main__":
    converter = Converter()
    print("Select from following currencies: ")
    print(converter.currencies)
    a = input("Convert from: ")
    count = int(input("Amount: "))
    b = input("Convert to: ")
    print(f"{count} {a} = {converter.convert(count, a, b)} {b} as of {converter.date()}")