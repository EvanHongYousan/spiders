__author__ = 'yantianyu'

from django.shortcuts import render
from django.http import HttpResponse

import requests

def home(request):
    url = 'http://www.douban.com/'
    response = requests.get(url)
    return HttpResponse(response)
