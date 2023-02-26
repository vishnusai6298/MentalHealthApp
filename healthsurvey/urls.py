from django.urls import path
from .views import form, submit, vatta, pitta, kapha,vatta_kapha,vatta_pitta,pitta_kapha,vatta_pitta_kapha,none

urlpatterns = [
    path('', form, name='form'),
    path('survey/', submit, name='submit'),
    path('vatta/', vatta, name='vatta'),
    path('pitta/', pitta, name='pitta'),
    path('kapha/', kapha, name='kapha'),
    path('vatta_pitta/', vatta_pitta, name='vatta_pitta'),
    path('vatta_kapha/', vatta_kapha, name='vatta_kapha'),
    path('pitta_kapha/', pitta_kapha, name='pitta_kapha'),
    path('vatta_pitta_kapha/', vatta_pitta_kapha, name='vatta_pitta_kapha'),
    path('none/', none, name='none'),

]
