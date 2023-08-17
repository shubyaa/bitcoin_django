from django.shortcuts import redirect, render
from .API import coins, news
from pycoingecko import CoinGeckoAPI

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

cg = CoinGeckoAPI()


# Create your views here.
def index(request):
    news_list = []
    if request.user.is_authenticated:
        list_coins = coins.get_coin_list()

        # Paging of List of Coins
        page = request.GET.get('page', 1)
        paginator = Paginator(list_coins, 20)

        try:
            num = paginator.page(page)

        except PageNotAnInteger:
            num = paginator.page(1)

        except EmptyPage:
            num = paginator.page(paginator.num_pages)

        
        # Paging the list of News

        news_list = news.get_news()

        
        # Passing the final Context to the html page {{The Dynamic Data}}

        context = {
            'news_list' : news_list,
            'numbers' : num,
            'paginator' : paginator,
        }

        return render(request, 'index.html', context=context)
    else:
        return redirect('accounts:login')

def comments(request):
    if request.user.is_authenticated:
        return render(request, 'comments.html')
    else:
        return redirect('accounts:login')