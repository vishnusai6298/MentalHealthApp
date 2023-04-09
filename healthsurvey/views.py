from django.shortcuts import render, redirect
from .forms import MentalHealthSurveyForm, PhysicalSurveyForm, PhysicalDoshaSurveyForm

guna = ""
mentaldosha = ""
physicaldosha = ""


def submit_physical(request):
    if request.method == 'POST':
        form = PhysicalDoshaSurveyForm(request.POST)
        if form.is_valid():
            vatta_count = 0
            pitta_count = 0
            kapha_count = 0
            for field in form:
                if field.name.startswith('q'):
                    answer = form.cleaned_data[field.name]
                    if answer == 'Vatta':
                        vatta_count += 1
                    elif answer == 'Pitta':
                        pitta_count += 1
                    elif answer == 'Kapha':
                        kapha_count += 1
            print("vatta_count"+str(vatta_count))
            print("pitta_count"+str(pitta_count))
            print("kapha_count"+str(kapha_count))
            if vatta_count >= 30:
                physicaldosha = 'vatta'
                return redirect('vatta1')
            elif pitta_count >= 30:
                physicaldosha = 'pitta'
                return redirect('pitta1')
            elif kapha_count >= 30:
                physicaldosha = 'kapha'
                return redirect('kapha1')
            elif vatta_count >= 20 and kapha_count >= 12:
                physicaldosha = 'vatta-kapha'
                return redirect('vatta_kapha1')
            elif vatta_count >= 20 and pitta_count >= 12:
                physicaldosha = 'vatta-pitta'
                return redirect('vatta_pitta1')
            elif pitta_count >= 20 and kapha_count >= 12:
                physicaldosha = 'pitta-kapha'
                return redirect('pitta_kapha1')
            else:
                return redirect('vatta_pitta_kapha1')
    else:
        form = PhysicalDoshaSurveyForm()
        return render(request, 'survey/survey6.html', {'form': form})
        # return redirect('form')


def submit_mentaldosha(request):
    if request.method == 'POST':
        form = MentalHealthSurveyForm(request.POST)
        if form.is_valid():
            vatta_count = 0
            pitta_count = 0
            kapha_count = 0
            for field in form:
                if field.name.startswith('q'):
                    answer = form.cleaned_data[field.name]
                    if answer == 'Vatta':
                        vatta_count += 1
                    elif answer == 'Pitta':
                        pitta_count += 1
                    elif answer == 'Kapha':
                        kapha_count += 1
            print("vatta_count"+str(vatta_count))
            print("pitta_count"+str(pitta_count))
            print("kapha_count"+str(kapha_count))
            if vatta_count >= 7:
                mentaldosha = 'vatta'
                return redirect('vatta')
            elif pitta_count >= 7:
                mentaldosha = 'pitta'
                return redirect('pitta')
            elif kapha_count >= 7:
                mentaldosha = 'kapha'
                return redirect('kapha')
            elif vatta_count >= 5 and kapha_count >= 5:
                mentaldosha = 'vatta-kapha'
                return redirect('vatta_kapha')
            elif vatta_count >= 5 and pitta_count >= 5:
                mentaldosha = 'vatta-pitta'
                return redirect('vatta_pitta')
            elif pitta_count >= 5 and kapha_count >= 5:
                mentaldosha = 'pitta-kapha'
                return redirect('pitta_kapha')
            else:
                return redirect('vatta_pitta_kapha')
    else:
        form = MentalHealthSurveyForm()
        return render(request, 'survey/mentalDoshaSurvey.html', {'form': form})
        # return redirect('form')


def home(request):
    return render(request, 'survey/home.html')


def form_physical(request):
    form = PhysicalSurveyForm()
    return render(request, 'survey/survey5.html', {'form': form})


def submit_guna(request):
    if request.method == 'POST':
        form = PhysicalSurveyForm(request.POST)
        if form.is_valid():
            sattva_count = 0
            rajas_count = 0
            tamas_count = 0
            for field in form:
                if field.name.startswith('q'):
                    answer = form.cleaned_data[field.name]
                    if answer == 'Sattva':
                        sattva_count += 1
                    elif answer == 'Rajas':
                        rajas_count += 1
                    elif answer == 'Tamas':
                        tamas_count += 1
            print("sattva_count"+str(sattva_count))
            print("rajas_count"+str(rajas_count))
            print("tamas_count"+str(tamas_count))
            if sattva_count >= 18:
                guna = 'sattva'
                return redirect('sattva')
            elif rajas_count >= 18:
                guna = 'rajas'
                return redirect('rajas')
            elif tamas_count >= 18:
                guna = 'tamas'
                return redirect('tamas')
            elif sattva_count >= 12 and tamas_count >= 8:
                guna = 'sattva-tamas'
                return redirect('sattvic_tamas')
            elif sattva_count >= 12 and rajas_count >= 8:
                guna = 'sattva-rajas'
                return redirect('sattvic_rajas')
            elif rajas_count >= 12 and tamas_count >= 8:
                guna = 'rajas-tamas'
                return redirect('rajas_tamas')
            else:
                guna = 'sattva-rajas-tamas'
                return redirect('vatta_pitta_kapha')
    else:
        form = PhysicalSurveyForm()
        return render(request, 'survey/survey5.html', {'form': form})


def sattvic_tamas(request):
    return render(request, 'survey/sattvic_tamas.html')


def sattvic_rajas(request):
    return render(request, 'survey/sattvic_rajas.html')


def rajas_tamas(request):
    return render(request, 'survey/rajas_tamas.html')


def vatta(request):
    return render(request, 'survey/vatta.html')


def vatta1(request):
    return render(request, 'survey/vatta1.html')


def sattva(request):
    return render(request, 'survey/sattva.html')


def rajas(request):
    return render(request, 'survey/rajas.html')


def tamas(request):
    return render(request, 'survey/tamas.html')


def pitta(request):
    return render(request, 'survey/pitta.html')


def kapha(request):
    return render(request, 'survey/kapha.html')


def vatta_kapha(request):
    return render(request, 'survey/vatta_kapha.html')


def vatta_pitta(request):
    return render(request, 'survey/vatta_pitta.html')


def pitta_kapha(request):
    return render(request, 'survey/pitta_kapha.html')


def vatta_pitta_kapha(request):
    return render(request, 'survey/vatta_pitta_kapha.html')


def none(request):
    return render(request, 'survey/none.html')


def pitta1(request):
    return render(request, 'survey/pitta1.html')


def kapha1(request):
    return render(request, 'survey/kapha1.html')


def vatta_kapha1(request):
    return render(request, 'survey/vatta_kapha1.html')


def vatta_pitta1(request):
    return render(request, 'survey/vatta_pitta1.html')


def pitta_kapha1(request):
    return render(request, 'survey/pitta_kapha1.html')


def vatta_pitta_kapha1(request):
    return render(request, 'survey/vatta_pitta_kapha1.html')
