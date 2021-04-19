from datetime import datetime
import requests


class ExchangeRateApi:
    def __init__(self):
        self._base_url = "https://api.exchangerate.host"

    def get_rates(self):
        url = f"{self._base_url}/latest"
        response = requests.get(url)
        return response.json()


class Converter:
    def __init__(self, api):
        self.data = api.get_rates()
        self.rates = self.data["rates"]
        self.currencies = list(self.rates.keys())
        self.success = self.data["success"]

    def convert(self, count, from_curr, to_curr):
        if self.success:
            if from_curr != "EUR":
                count = count / self.rates[from_curr]
            return f"{self.rates[to_curr]*count:.4f}"
        return "Conversion Failed."

    def date(self):
        date = str(self.data["date"])
        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%d.%m.%Y")
        return date


def main():
    converter = Converter(ExchangeRateApi())
    print("Select from following currencies: ")
    print(converter.currencies)
    from_curr = input("Convert from: ")
    count = int(input("Amount: "))
    to_curr = input("Convert to: ")
    print(f"{count} {from_curr} = {converter.convert(count, from_curr, to_curr)} \
{to_curr} as of {converter.date()}")


if __name__ == "__main__":
    main()