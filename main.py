import requests
from bs4 import BeautifulSoup

def search(currency_list, name):
    for i in range(0, len(currency_list)):
        if currency_list[i].name == name:
            return currency_list[i]
    return None
        
def display_all(currency_list):
    for i in range(0, len(currency_list)):
        print("Index: " + str(i))
        currency_list[i].display_info()
        print()

class Currency:
    def __init__(self, name, symbol, price, market_cap):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.market_cap = market_cap
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Symbol: {self.symbol}")
        print(f"Price: {self.price}")
        print(f"Market Cap: {self.market_cap}")

url = "https://coinmarketcap.com/"
name_class = "kKpPOn"
symbol_class = "coin-item-symbol"
price_class = "ejtlWy"
market_cap_class = "bCdPBp"

request = requests.get(url)
html = BeautifulSoup(request.text, "html.parser")

names = html.find_all("p", {"class": name_class})
symbols = html.find_all("p", {"class": symbol_class})
prices = html.find_all("div", {"class": price_class})
market_caps = html.find_all("span", {"class": market_cap_class})

currency_list = []

for i in range(0, len(names)):
    currency_list.append(Currency(names[i].text, symbols[i].text, prices[i].text, market_caps[i].text))

input_name = ""
while input_name != "0":
    input_name = input("Enter the currency name (1 - print all, 0 - exit): ")
    print()

    if (input_name == "1"):
        display_all(currency_list)
    elif (input_name == "0"):
        break
    else:
        result = search(currency_list, input_name)
        if (result is not None):
            result.display_info()
            print()
        else:
            print("Currency not found\n")