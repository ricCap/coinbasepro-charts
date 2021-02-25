import requests
import webbrowser
import matplotlib.pyplot as plt
import mpld3

from cbprocharts.procharter import ProCharter

CURRENCIES_ENDPOINT = "https://api.exchangeratesapi.io/latest?base={}"


class Balance:
    """A class that holds a portfolio balance and is able to compute crypto
    conversions based on added rates"""

    def __init__(self, charter: ProCharter):
        self.balance = dict()
        self.rates = dict()
        self.currency_rates = dict()
        self.charter = charter

    def add_currency_rate(self, base: str, target: str) -> bool:
        """Get the current currency conversion rate

        Args:
            from (str): base currency.
            to (str): target currency.
        Returns:
            bool: whether the retrieval of the rate was successful
        """
        rates = requests.get(CURRENCIES_ENDPOINT.format(base))
        try:
            self.currency_rates[base] = float(rates.json()["rates"][target])
        except KeyError:
            return False
        return True

    def add_rate(self, base: str, target: str) -> bool:
        """Get the current conversion rate between two crypto

        Args:
            from (str): base crypto.
            to (str): target crypto.
        Returns:
            bool: whether the retrieval of the rate was successful
        """
        crypto_pair = "{}-{}".format(base, target)
        try:
            self.rates[crypto_pair] = float(self.charter.get_product_ticker(crypto_pair)[
                "price"])
        except KeyError:
            return False
        return True

    def compute_euro_balance(self):
        """Try to convert all crypto to euro"""
        accounts = self.charter.get_accounts()
        balance = dict()
        print(accounts)
        for crypto in accounts:
            quantity = float(crypto["balance"])
            if quantity > 0:
                cryptoName = crypto["currency"]
                price_EUR = self.charter.get_product_ticker(
                    cryptoName + "-EUR")

                try:
                    balance[cryptoName] = quantity * float(price_EUR["price"])
                except KeyError:
                    try:
                        price_BTC = self.charter.get_product_ticker(
                            cryptoName + "-BTC")["price"]
                        balance[cryptoName] = quantity * \
                            float(price_BTC) * self.rates["BTC-EUR"]
                    except KeyError:
                        # Should check ffor USDC
                        balance[cryptoName] = 0.
        self.balance = balance

    def show(self):
        """Show the current balance"""
        body = ""
        # Sort balance
        balance = dict(sorted(self.balance.items(), key=lambda item: item[1]))

        # Total balance euro
        total_euro = sum(balance.values())
        body += "<p>Your current portfolio is worth €{}</p>".format(total_euro)

        # Generate chart
        fig, ax = plt.subplots()
        ax.pie(balance.values(), labels=balance.keys(), autopct='%1.1f%%',
               startangle=90)
        # Equal aspect ratio ensures that pie is drawn as a circle.
        ax.axis('equal')
        body += mpld3.fig_to_html(fig)

        # Add table with values
        body += "<p>{}</p>".format(balance)

        html = """<html>
        <head></head>
        <body>{}</body>
        </html>"""
        with open('report.html', 'w') as file:
            file.write(html.format(body))

        webbrowser.open_new_tab('report.html')
