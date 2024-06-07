# breweries/views.py
import requests
from django.shortcuts import render
from django.http import HttpResponseBadRequest

def breweries_view(request):
    url = 'https://api.openbrewerydb.org/breweries'
    params = {}
    
    country = request.GET.get('country')
    city = request.GET.get('city')

    if country:
        params['by_country'] = country
    if city:
        params['by_city'] = city

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
    else:
        return HttpResponseBadRequest("Error al obtener datos de la API")

    context = {
        'breweries': data,
        'selected_country': country,
        'selected_city': city
    }

    return render(request, 'breweries/breweries.html', context)
