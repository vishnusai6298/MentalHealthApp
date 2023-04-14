from django.urls import path
from .views import home, results, vatta1, kapha1, pitta1, vatta_kapha1, vatta_pitta1, pitta_kapha1, vatta_pitta_kapha1, submit_physical, submit_mentaldosha, sattvic_rajas, sattvic_tamas, rajas_tamas, sattva, rajas, tamas, vatta, pitta, kapha, vatta_kapha, vatta_pitta, pitta_kapha, vatta_pitta_kapha, none, form_physical, submit_guna

urlpatterns = [
    # path('form', form_physical, name='form_physical'),
    path('', home, name='home'),
    path('mentaldoshasurvey/', submit_mentaldosha, name='submit_mentaldosha'),
    path('gunasurvey/', submit_guna, name='submit_guna'),
    path('physicaldoshasurvey/', submit_physical,
         name='submit_physical'),
    path('results/', results, name='results'),

    path('vatta/', vatta, name='vatta'),
    path('pitta/', pitta, name='pitta'),
    path('kapha/', kapha, name='kapha'),
    path('vatta_pitta/', vatta_pitta, name='vatta_pitta'),
    path('vatta_kapha/', vatta_kapha, name='vatta_kapha'),
    path('pitta_kapha/', pitta_kapha, name='pitta_kapha'),
    path('vatta_pitta_kapha/', vatta_pitta_kapha, name='vatta_pitta_kapha'),
    path('vatta1/', vatta1, name='vatta1'),
    path('pitta1/', pitta1, name='pitta1'),
    path('kapha1/', kapha1, name='kapha1'),
    path('vatta_pitta1/', vatta_pitta1, name='vatta_pitta1'),
    path('vatta_kapha1/', vatta_kapha1, name='vatta_kapha1'),
    path('pitta_kapha1/', pitta_kapha1, name='pitta_kapha1'),
    path('vatta_pitta_kapha1/', vatta_pitta_kapha1, name='vatta_pitta_kapha1'),
    path('none/', none, name='none'),
    path('sattva/', sattva, name='sattva'),
    path('rajas/', rajas, name='rajas'),
    path('tamas/', tamas, name='tamas'),
    path('sattvic_rajas/', sattvic_rajas, name='sattvic_rajas'),
    path('sattvic_tamas/', sattvic_tamas, name='sattvic_tamas'),
    path('rajas_tamas/', rajas_tamas, name='rajas_tamas'),
]
