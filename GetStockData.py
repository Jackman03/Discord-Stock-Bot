#Web scraping. I dont care if its illegal.
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def GetCurrentPrice(Ticker):
    url = 'https://finance.yahoo.com/quote/' + Ticker +'/'

    r = requests.get(url)

    if r.status_code == 200:
        texts = BeautifulSoup(r.text,'html.parser')

        try:
            price = texts.find('fin-streamer', {'data-field': 'regularMarketPrice'}).text
            change = texts.find('fin-streamer', {'data-field': 'regularMarketChangePercent'}).text
            return price, change
        except AttributeError:
            print("Failed to locate stock price or change data. Website structure may have changed.")

    #404 error indicates page not found. So in our case it would likely be invalid ticker 
    elif r.status_code == 404:
        print("Invalid ticker. Please try again")
    else:
        print("Web error: ",r.status_code)





Stock = 'VOO'
#Yahoo works better when we use all caps
Curtime = datetime.now()
Curtime = Curtime.strftime("%H:%M:%S")
CurPrice = GetCurrentPrice(Stock)

print(f"{CurPrice[0]} at {Curtime}")
