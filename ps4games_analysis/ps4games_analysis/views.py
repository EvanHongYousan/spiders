__author__ = 'yantianyu'

from django.shortcuts import render
from django.http import HttpResponse

import urllib
import urllib.request

def home(request):
    data = {}
    data['word'] = 'Jecvay Nodtes'

    url_values = urllib.parse.urlencode(data)
    url = 'http://www.baidu.com/s?'
    full_url = url+url_values

    data = urllib.request.urlopen(full_url).read()
    data = data.decode('UTF-8')

    return HttpResponse(data)
