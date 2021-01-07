import requests
import json

URL = 'https://api.monobank.ua/bank/currency'

res = requests.get(URL)
exchanges = json.loads(res.text)


class Currency:
    def __init__(self,buy,sell):
        self.buy = buy
        self.sell = sell

    def exchangeRate(self,newCurrency):
        return self.sell / newCurrency.buy

    def buyCurrency(self,newCurrency,count):
        newValue = count * self.sell / newCurrency.buy
        return round(newValue, 3)


currencyUSD = Currency(exchanges[0]["rateSell"],exchanges[0]["rateBuy"])
currencyEUR = Currency(exchanges[1]["rateSell"],exchanges[1]["rateBuy"])
currencyRUB = Currency(exchanges[2]["rateSell"],exchanges[2]["rateBuy"])
currencyUAH = Currency(1,1)

currencyList = {'USD' : currencyUSD, 'EUR' : currencyEUR, 'RUB' : currencyRUB,'UAH' : currencyUAH}