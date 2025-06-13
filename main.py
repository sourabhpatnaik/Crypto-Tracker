import requests
import json


def crypto_menu():
    print("====================")
    print("  Crypto Tracker")
    print("====================")

    print("1. Search Cryptocurrency")
    print("2. Save Result to File")
    print("3. Exit")
    print("====================")

crypto_menu()
choice = int(input("Enter your choice: "))





def crypto_search():
    cryptoName = input("Enter Cryptocurrency Name: ")
    currency = input("Enter Your desired Currency: ")

    base_url = "https://api.coingecko.com/api/v3/coins/markets?"
    parameters = {
    "ids":"{}".format(cryptoName),
    "vs_currency": "{}".format(currency),
    }

    response = requests.get(base_url, params=parameters)
    cryptoData = response.json()
    # print(json.dumps(cryptoData,indent=4))

    if response.status_code == 200:

        name = cryptoData[0]['name']
        marketPrice = cryptoData[0]['current_price']
        marketCap = cryptoData[0]['market_cap']
        high_24h = cryptoData[0]['high_24h']
        low_24h = cryptoData[0]['low_24h']
        priceChange_percentage = cryptoData[0]['price_change_percentage_24h']

        print("\n====================")
        print("Cryptocurrency Details")
        print(f"Name: {name}")
        print(f"Market Price: {marketPrice} {currency.upper()}") 
        print(f"Market Cap: {marketCap} {currency.upper()}")
        print(f"High 24h: {high_24h} {currency.upper()}")
        print(f"Low 24h: {low_24h} {currency.upper()}") 
        print(f"Price Change (24h): {priceChange_percentage}%")
        print("====================\n")
           
    elif response.status_code == 404:
        print("Cryptocurrency not found. Please check the name and try again.")
    
    elif response.status_code == 400:
     print("Bad Request. Please check the parameters and try again.")

    else:
        print("Enter Valid Cryptocurrency")
        
        


while choice != 3:
    if choice == 1:
        crypto_search()

    elif choice == 2:
        print("Feature not implemented yet.")       
    else:
        print("Invalid choice. Please try again.")

    crypto_menu()
    choice = int(input("Enter your choice: "))




    






