from django import forms

class MentalHealthSurveyForm(forms.Form):
    feeling = forms.IntegerField(label='How are you feeling today?')
    stress = forms.IntegerField(label='On a scale of 1-10, how much stress are you feeling?')
    coping_mechanisms = forms.IntegerField(label='What coping mechanisms do you use to manage your mental health?')
