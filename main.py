import requests
import json

cryptoName = input("Enter Cryptocurrency Name: ").lower()
currency = input("Enter Your desired Currency: ").lower()

base_url = "https://api.coingecko.com/api/v3/coins/markets?"
parameters = {
    "ids":"{}".format(cryptoName),
    "vs_currency": "{}".format(currency),
}

response = requests.get(base_url, params=parameters)
cryptoData = response.json()
# print(json.dumps(cryptoData,indent=4))

if response.status_code == 200:
    if cryptoData:  # Check if the list is not empty
        name = cryptoData[0]['name']
        marketPrice = cryptoData[0]['current_price']
        marketCap = cryptoData[0]['market_cap']
        high_24h = cryptoData[0]['high_24h']
        low_24h = cryptoData[0]['low_24h']
        priceChange_percentage = cryptoData[0]['price_change_percentage_24h']
        
        print(f"Name: {name}")
        print(f"Market Price: {marketPrice} {currency.upper()}") 
        print(f"Market Cap: {marketCap} {currency.upper()}")
        print(f"High 24h: {high_24h} {currency.upper()}")
        print(f"Low 24h: {low_24h} {currency.upper()}") 
        print(f"Price Change (24h): {priceChange_percentage}%")
    else:
        print("Cryptocurrency not found. Please check the name and try again.")

