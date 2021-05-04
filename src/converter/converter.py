from datetime import datetime
import requests


class ExchangeRateApi:
    """Luokka, joka hallinnoi API:n käyttöä."""

    def __init__(self):
        self._base_url = "https://api.exchangerate.host"

    def get_rates(self):
        """Antaa uusimmat valuuttojen kurssit API:sta.

        Returns:
            Valuuttakurssit sanakirja muodossa.
        """

        url = f"{self._base_url}/latest"
        response = requests.get(url)
        return response.json()


class Converter:
    """Hoitaa API:n arvojen käsittelemisen ja hoitaa valuutanvaihdon näillä arvoilla."""

    def __init__(self, api):
        """Luokan konstruktori. Tallentaa API:lta saadut olennaiset tiedot helpoiksi muuttujiksi.

        Args:
            api: Saa ExhangeRateApi-luokan ja tätä kautta luo arvot valuutanvaihtoa varten.
        """

        self.data = api.get_rates()
        self.rates = self.data["rates"]
        self.currencies = list(self.rates.keys())
        self.success = self.data["success"]

    def convert(self, count, from_curr, to_curr):
        """Vaihtaa valuutan.

        Args:
            count: Vaihdettavan valuutan määrä.
            from_curr: Vaihdettava valuutta muodossa "USD" / "BTC".
            to_curr: Valuutta johon halutaan vaihtaa.

        Returns:
            Valuutan määrä johon ollaan vaihtamassa.
        """

        if self.success and count != "":
            if from_curr != "EUR":
                count = count / self.rates[from_curr]
            return f"{float(self.rates[to_curr])*count:.4f}")
        return False

    def date(self):
        """Antaa valuutanvaihdon ajankohdan.

        Returns:
            API:n vaihtotapahtuman antaman päivämäärän.
        """

        date = str(self.data["date"])
        date = datetime.strptime(date, "%Y-%m-%d")
        date = date.strftime("%d.%m.%Y")
        return date
