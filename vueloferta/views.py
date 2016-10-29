# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse

from django.shortcuts import render
import httplib, urllib, re, time
from lxml import html

url = 'http://www.vueloferta.com.usrfiles.com/html/0e7438_3222f762bf226935501d3685dc0de84d.html'


def index(request):
    data = getData()
    return HttpResponse(data, content_type='application/json')

def getData():

    # TODO: falta agregar exceptiones
    response = urllib.urlopen(url)

    if response.code == 200:
        return parserTable(response.read())
    else:
        return []

def parserTable(source):
    data = []
    tree = html.fromstring(source)
    cells = tree.xpath('//tr[not (@bgcolor="#CCCCCC")]')

    # si modifican la pag, puede que esto no funcione
    for cell in cells:
        data.append({
            'destiny': getTextUrl(cell, 1),
            'url': getUrl(cell, 1),
            'price': getValue(cell, 2),
            'exchange': getValue(cell, 3),
            'discount': getValue(cell, 4)
        })

    return data


# Parse de ayuda para navegar en xpath
def getValue(root, index):
	for element in root.xpath('td['+str(index)+']'):
		return element.text

# Parse de ayuda para navegar en xpath
def getUrl(root, index):
	for element in root.xpath('td['+str(index)+']/a/@href'):
		return element

# Parse de ayuda para navegar en xpath
def getTextUrl(root, index):
	for element in root.xpath('td['+str(index)+']/a'):
		return element.text
