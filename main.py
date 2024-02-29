import requests
from bs4 import BeautifulSoup

name_class = "kKpPOn"
symbol_class = "coin-item-symbol"
price_class = "gDrtaY"
market_cap_class = "bCdPBp"

request = requests.get("https://coinmarketcap.com/")
html = BeautifulSoup(request.text, "html.parser")

names = html.find_all("p", {"class": name_class})
symbols = html.find_all("p", {"class": symbol_class})
prices = html.find_all("div", {"class": price_class})
market_caps = html.find_all("span", {"class": market_cap_class})

for name in names:
    print(name.text)

for symbol in symbols:
    print(symbol.text)

for price in prices:
    print(price.text)

for market_cap in market_caps:
    print(market_cap.text)