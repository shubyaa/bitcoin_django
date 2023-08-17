from pycoingecko import CoinGeckoAPI
from datetime import datetime


from .data_models import Coin

cg = CoinGeckoAPI()

def get_coin_list():

    values = cg.get_coins_markets(vs_currency='inr')
    list_of_coins = []

    for i in range(0, 100):
        element = values[i]

        id = element['id']
        symbol = element['symbol']
        image = element['image']
        current_price = element['current_price']
        res = ('{: ,}'.format(current_price))
        last_updated = element['last_updated']
        date = str(last_updated).split('T')
        sparkline = "https://www.coingecko.com/coins/{0}/sparkline".format(get_coin_sequence_number(image_url=image))
        coin = Coin(id, symbol, image, res, sparkline, date[0])
        

        list_of_coins.append(coin)
    return list_of_coins

def get_coin_last_month_price(id:str):
    date = []
    price = []
    data = cg.get_coin_market_chart_by_id(id, vs_currency='inr', days=30)
    
    for a in data['prices']:
        date_to_convert = datetime.fromtimestamp(a[0]/1000)
        date.append(str(date_to_convert.date()))
        price.append(a[1])
       

    return {
        'date' : date,
        'price' : price,
    }

def get_coin_last_one_day_price(id:str):
    data = cg.get_coin_market_chart_by_id(id, vs_currency='inr', days=1)

    prices = data['prices']
    market_cap = data['market_caps']
    volume_total = data['total_volumes']

    return prices
    
def get_coin_last_five_days_price(id:str):
    data = cg.get_coin_market_chart_by_id(id, vs_currency='inr', days=5)

    prices = data['prices']
    market_cap = data['market_caps']
    volume_total = data['total_volumes']

    return prices

def get_coin_last_six_month_price(id:str):
    data = cg.get_coin_market_chart_by_id(id, vs_currency='inr', days=180)

    prices = data['prices']
    market_cap = data['market_caps']
    volume_total = data['total_volumes']

    return prices



### Get The coin sequence from the urls
def get_coin_sequence_number(image_url):
    # TO generate Sparkline
    words = str(image_url).split('/')
    return words[5]

