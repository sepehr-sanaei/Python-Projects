import requests
import json
import pyttsx3
import time


api = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
api_read = json.loads(api.text)

btc_old = api_read['bpi']['USD']['rate']
btc_old_price = btc_old.replace(',', '')



while True:
    api_2 = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    api_read_2 = json.loads(api_2.text)
    btc = api_read_2['bpi']['USD']['rate']
    btc_price = btc.replace(',', '')
    engine = pyttsx3.init()
    if btc_price != btc_old_price:
        btc_new = float(btc_price)
        btc_past = float(btc_old_price)
        res = btc_new - btc_past
        res_round = round(res, 4)
        if res_round > 0 :
            print(f"Bitcoin price is {btc_new} dollars, and it raised {res_round} dollars")
            engine.say(f"Bitcoin price is {btc_new} dollars, and it raised {res_round} dollars")
        else:
            print(f"Bitcoin price is {btc_new} dollars, and it dropped {res_round} dollars")
            engine.say(f"Bitcoin price is {btc_new} dollars, and it  dropped {res_round} dollars")
        
        engine.runAndWait()
        btc_old_price = btc_price
        
        time.sleep(5)
                       