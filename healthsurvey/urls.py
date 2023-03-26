from django.urls import path
from .views import home, form, submit, vatta, pitta, kapha, vatta_kapha, vatta_pitta, pitta_kapha, vatta_pitta_kapha, none, form_physical, submit_physical

urlpatterns = [
    path('form', form_physical, name='form_physical'),
    path('', home, name='home'),
    path('survey/', submit, name='submit'),
    path('physicalsurvey/', submit_physical, name='submit_physical'),
    path('vatta/', vatta, name='vatta'),
    path('pitta/', pitta, name='pitta'),
    path('kapha/', kapha, name='kapha'),
    path('vatta_pitta/', vatta_pitta, name='vatta_pitta'),
    path('vatta_kapha/', vatta_kapha, name='vatta_kapha'),
    path('pitta_kapha/', pitta_kapha, name='pitta_kapha'),
    path('vatta_pitta_kapha/', vatta_pitta_kapha, name='vatta_pitta_kapha'),
    path('none/', none, name='none'),

]
