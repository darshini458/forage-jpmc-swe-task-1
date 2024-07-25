import json
import random
import urllib.request
import time


QUERY = "http://localhost:8080/query?id={}"  


N = 5

def getDataPoint(quote):
    """ Produce all the needed values to generate a datapoint """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    """ Get ratio of price_a and price_b """
    return price_a / price_b if price_b != 0 else None

if __name__ == "__main__":
    while True: 
        try:
            quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
            
            prices = {}
            for quote in quotes:
                stock, bid_price, ask_price, price = getDataPoint(quote)
                prices[stock] = price
                print(f"Quoted {stock} at (bid:{bid_price}, ask:{ask_price}, price:{price})")
            
            if "ABC" in prices and "DEF" in prices:
                ratio = getRatio(prices['ABC'], prices['DEF'])
                if ratio is not None:
                    print(f"Ratio {ratio}")
                else:
                    print("Price of DEF is zero, cannot compute ratio.")
            else:
                print("Required stocks are not available in the quotes.")
        
        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(N)  
