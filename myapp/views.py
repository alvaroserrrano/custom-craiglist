from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models

BASE_CRAIGLIST_URL = 'https://detroit.craigslist.org/search/?query='
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url=f'{BASE_CRAIGLIST_URL}{quote_plus(search)}'
    # print(final_url)
    response = requests.get(final_url)
    data = response.text
    # print(data)
    soup = BeautifulSoup(data, features='html.parser')
    results = soup.find_all('li', {'class':'result-row'})
    final_results = []
    for result in results:
        result_title = result.find(class_='result-title').text
        result_url = result.find('a').get('href')
        if result.find(class_='result-price'):
            result_price =result.find(class_='result-price').text
        else:
            result_price = 'N/A'
        if result.find(class_='result-image').get('data-ids'):
            result_image_id=result.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            result_image_url=BASE_IMAGE_URL.format(result_image_id)
            print(result_image_url)
        else:
            result_image_url = 'https://craigslist.org/images/peace.jpg'
        final_results.append((result_title, result_url, result_price, result_image_url))

    context={
        'final_results': final_results,
        'search': search,
    }
    return render(request, 'myapp/new_search.html', context)
