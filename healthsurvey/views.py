'''
from django.shortcuts import render
from .forms import MentalHealthSurveyForm

def survey_view(request):

    if request.method == 'POST':

        form = MentalHealthSurveyForm(request.POST)
        if form.is_valid():
            
            feeling = form.cleaned_data['feeling']
            stress = form.cleaned_data['stress']
            coping_mechanisms = form.cleaned_data['coping_mechanisms']
            #response = SurveyResponse(user=request.user, feeling=feeling, stress=stress, coping_mechanisms=coping_mechanisms)
            #response.save()            
            # Perform actions based on survey inputs
            if stress > 7:
                recommended_action = "Consider talking to a therapist or counselor."
            else:
                recommended_action = "Keep up with your current coping mechanisms."
            
            return render(request, 'survey/results.html', {'recommended_action': recommended_action})
    else:
        form = MentalHealthSurveyForm()
    return render(request, 'survey/survey.html', {'form': form})
    '''

from django.shortcuts import render, redirect
from .forms import MentalHealthSurveyForm

def form(request):
    form = MentalHealthSurveyForm()
    return render(request, 'survey/survey2.html', {'form': form})

def submit(request):
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
            if vatta_count >=7:
                return redirect('vatta')
            elif pitta_count >=7:
                return redirect('pitta')
            elif kapha_count>=7:
                return redirect('kapha')
            elif vatta_count>=5 and kapha_count>=5:
                return redirect('vatta_kapha')
            elif vatta_count>=5 and pitta_count>=5:
                return redirect('vatta_pitta')
            elif pitta_count>=5 and kapha_count>=5:
                return redirect('pitta_kapha')
            elif vatta_count>=3 and pitta_count>=3 and kapha_count>=3:
                return redirect('vatta_pitta_kapha')
            else:
                return redirect('none')   
    else:
        return redirect('form')

def vatta(request):
    return render(request, 'survey/vatta.html')

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

    
