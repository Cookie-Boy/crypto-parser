import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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

def search(currency_list, name):
    for i in range(0, len(currency_list)):
        if currency_list[i].name.lower() == name.lower():
            return currency_list[i]
    return None
        
def display_all(currency_list):
    for i in range(0, len(currency_list)):
        print("Index: " + str(i))
        currency_list[i].display_info()
        print()

url = "https://coinmarketcap.com/"
cmc_table_class = "cmc-table"
name_class = "kKpPOn"
symbol_class = "coin-item-symbol"
price_class = "cAhksY"
market_cap_class = "bCdPBp"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)

for i in range(15):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.5)

names = driver.find_elements(By.XPATH, f"//table[contains(@class, '{cmc_table_class}')]//p[contains(@class, '{name_class}')]")
symbols = driver.find_elements(By.XPATH, f"//table[contains(@class, '{cmc_table_class}')]//p[contains(@class, '{symbol_class}')]")
prices = driver.find_elements(By.XPATH, f"//table[contains(@class, '{cmc_table_class}')]//div[contains(@class, '{price_class}')]")
market_caps = driver.find_elements(By.XPATH, f"//table[contains(@class, '{cmc_table_class}')]//span[contains(@class, '{market_cap_class}')]")

currency_list = []

for i in range(0, len(names)):
    currency_list.append(Currency(names[i].text, symbols[i].text, prices[i].text, market_caps[i].text))

driver.close()
driver.quit()

os.system("cls")
input_name = ""
while (input_name != "0"):
    input_name = input("Enter the currency name (1 - print all, 0 - exit): ")
    print()

    if (input_name == "1"):
        display_all(currency_list)
    elif (input_name != "0"):
        result = search(currency_list, input_name)
        if (result is not None):
            result.display_info()
            print()
        else:
            print("Currency not found\n")