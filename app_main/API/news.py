from newscatcherapi import NewsCatcherApiClient
from .data_models import News
from dotenv import load_dotenv
import os
from bitcoin import settings

# Load Environment Variables
load_dotenv(os.path.join(settings.BASE_DIR, 'bitcoin/.env'))

# To generate an api key for news visit 
# https://newscatcherapi.com/news-api
API_KEY = os.environ.get('API_KEY')     # API_KEY for news api

client = NewsCatcherApiClient(x_api_key=API_KEY)

list_of_news = []

def get_news():

    search = client.get_search(topic='finance', lang='en', page_size=5, q="Crypto",countries=['IN','ENG', 'USA'])

    # Add the details and save it in News object

    for i in search['articles']:

        news = News(i['title'], i['media'], i['link'], i['summary'])
        list_of_news.append(news)

    return list_of_news