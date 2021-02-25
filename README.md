# cbprocharts

Some nice charts to show if what you are doing on CoinbasePro is GOOD or BAD!!! If you also think that CoinbasePro lacks of some basic charts and information to understand how to A wrapper of the [cbpro](https://github.com/danpaquin/coinbasepro-python) client.

# Project status

I am still building the foundations, but I plan to build at least some html reports and have an example with a small http server for simple interaction.

# Requirements

We are still figuring out what we want to implement. Please feel free to open an issue and tell us what you would like to have.

Currently we want to:

- Have a chart that shows all portfolio positions in EUR and BTC
- Show changes in the portfolio(%) of various assets (between two different dates)
- Show average entry price of portfolio assets

# Installation

Tested with python3.8.5\. Put your key in the configuration file. If you feel like protecting your private key, you should change permissions and call the go.py script with the correct permissions. Note that this library is a wrapper of the [cbpro](https://github.com/danpaquin/coinbasepro-python) client, and has all its functionalities; namely, you can initialize and use what we implement while having direct access to the cbpro client.

# Contributors

Just me for now. However, if someone starts or has the intention to use this library please reach out. I'd love to improve it and make it available to other people. Suggestions and improvements can also be proposed by simply opening an issue.
