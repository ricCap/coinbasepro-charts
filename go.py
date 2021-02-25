import cbprocharts
import json
import getpass

config_file = "./config.json"

with open('config.json') as file:
    api_config = json.load(file)
passphrase = getpass.getpass()

charter = cbprocharts.ProCharter(
    api_config["api_key"], api_config["api_secret"], passphrase)

balance = cbprocharts.Balance(charter)
balance.add_currency_rate("USD", "EUR")
balance.add_rate("BTC", "EUR")

balance.compute_euro_balance()
balance.show()
