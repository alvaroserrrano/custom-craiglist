from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'base.html')

def new_search(request):
    return HttpResponse('Hello from new search')
