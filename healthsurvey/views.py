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
