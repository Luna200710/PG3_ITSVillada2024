from django.urls import path
from .views import breweries_view

urlpatterns = [
    path('', breweries_view, name='breweries'),
]