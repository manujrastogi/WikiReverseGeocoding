# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from HTMLParser import HTMLParser
from utils import MyHtmlParser
from urllib import FancyURLopener
from BeautifulSoup import BeautifulSoup
from wikigeocoding.settings import PROJECT_PATH

class MyOpener(FancyURLopener):
    version='Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'

def home(request):
    return render(request, 'home.html', locals())

def parse_url(request):
    url = request.GET.get('url', None)
    #opener = open(PROJECT_PATH + '/List_of_highest_mountains', 'r+')
    #parser = MyHtmlParser()
    #data = parser.feed(''.join(opener.readlines()))
    myopener = MyOpener()
    opener = myopener.open(url)
    soup = BeautifulSoup(''.join(opener.readlines()))
    longitude = []
    latitude = []
    # u'86\xb055\u203231\u2033E'
    log = soup.findAll('span', {'class':"longitude"})
    lat = soup.findAll('span', {'class':"latitude"})
    for i in log:
        v = i.string
        degree = v.split(u'\xb0')[0]
        minute = v.split(u'\u2032')[0].split(u'\xb0')[1]
        sec = v.split(u'\u2033')[0].split(u'\u2032')[1].split(u'\xb0')[0]
        sign = v.split(u'\u2033')[1]
        if sign in (u'S', u'W'):
            log_value = -1 * (float(degree) + (float(minute)/60) + (float(sec)/3600))
        else:
            log_value = float(degree) + (float(minute)/60) + (float(sec)/3600)
        longitude.append(log_value)
    for i in lat:
        v = i.string
        degree = v.split(u'\xb0')[0]
        minute = v.split(u'\u2032')[0].split(u'\xb0')[1]
        sec = v.split(u'\u2033')[0].split(u'\u2032')[1].split(u'\xb0')[0]
        sign = v.split(u'\u2033')[1]
        if sign in (u'S', u'E'):
            lat_value = -1 * (float(degree) + (float(minute)/60) + (float(sec)/3600))
        else:
            lat_value = float(degree) + (float(minute)/60) + (float(sec)/3600)
        latitude.append(lat_value)
    values = []
    for lat in latitude:
        for lng in longitude:
            d = []
            d.append(lat)
            d.append(lng)
            break;
        values.append(d)
    #values = zip(latitude,longitude)
    values = values[:5]
    opener.close()
    return render(request, 'map.html',locals())


#def geo_map(request):
#    return render(request, 'map.html',locals())