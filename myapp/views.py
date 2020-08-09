from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus

BASE_CRAIGLIST_URL = 'https://detroit.craigslist.org/search/?query={}'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    final_url=f'BASE_CRAIGLIST_URL{quote_plus(search)}'
    print(final_url)
    context={
        'search': search
    }
    return render(request, 'myapp/new_search.html', context)
