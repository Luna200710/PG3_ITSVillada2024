import requests
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseBadRequest

def home(request):
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

    return render(request, 'breweries.html', context)

class ejercicio2(TemplateView):
    template_name = "ejercicio2.html"

    def get_context_data(self, **kwargs: any):
        context = super().get_context_data(**kwargs)
        res = requests.get("https://www.cultura.gob.ar/api/v2.0/museos/")
        res_json = res.json()
        museos_res = res_json.get('results')
        context['museos'] = museos_res
        return context