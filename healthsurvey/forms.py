from django import forms


class MentalHealthSurveyForm(forms.Form):
    '''
    feeling = forms.IntegerField(label='How are you feeling today?')
    stress = forms.IntegerField(label='On a scale of 1-10, how much stress are you feeling?')
    coping_mechanisms = forms.IntegerField(label='What coping mechanisms do you use to manage your mental health?')
    '''

    q1 = forms.ChoiceField(
        label="Memory:Which of the following best describes your memory",
        choices=(('Vatta', 'I have some difficulty in remembering things'), ('Pitta', 'I have a good memory in general'),
                 ('Kapha', 'I have a good memory, I can remember things from the past that not many other can')),
        widget=forms.RadioSelect)
    q2 = forms.ChoiceField(
        label="Concentration: How easy is it for you to focus on something or someone for an extended period of time",
        choices=(('Vatta', 'It is easy for me to get distracted'),
                 ('Pitta', 'I can focus if the matter is interesting and logical'),
                 ('Kapha', 'I usually have no trouble concentrating')),
        widget=forms.RadioSelect)
    q3 = forms.ChoiceField(
        label="Changes to Plans:How would you react if there was a sudden change in your schedule",
        choices=(('Vatta', 'I usually dont get angry, I am happy to go with the flow'),
                 ('Pitta', 'I would not be very happy but if made sense to me, I would be fine with it'),
                 ('Kapha', 'I dont like changes to my plans ')),
        widget=forms.RadioSelect)
    q4 = forms.ChoiceField(
        label="Appeal to change:What is the main reason you may be convinced to change your mind about something?",
        choices=(('Vatta', 'Overthinking and second guessing my decision'),
                 ('Pitta', 'Someone explains to me how I am wrong and convinces me through logic'),
                 ('Kapha', 'If a loved one or friend asks me to reconsider')),
        widget=forms.RadioSelect)
    q5 = forms.ChoiceField(
        label="Story-telling:How do you tell stories about events or experiences in your life?",
        choices=(('Vatta', 'My stories are elaborate and usually wander into several topics throughout the story'),
                 ('Pitta', 'I am to the point the precise and I focus only on the important things'),
                 ('Kapha', 'I can give detailed descriptions of what happned and how')),
        widget=forms.RadioSelect)
    q6 = forms.ChoiceField(
        label="Style of work:Which of the following best describes your style of work?",
        choices=(('Vatta', 'I have some difficulty in remembering things'), ('Pitta', 'I have a good memory in general'),
                 ('Kapha', 'I have a good memory, I can remember things from the past that not many other can')),
        widget=forms.RadioSelect)
    q7 = forms.ChoiceField(
        label="Learning:Which of the following best describes how you learn a new concept?",
        choices=(('Vatta', 'I have bouts of creativity and work and bouts where I am easily distracted'),
                 ('Pitta', 'I work in accordance to a proper schedule even when I dont need to'),
                 ('Kapha', 'I start slow and pick up pace as I start working')),
        widget=forms.RadioSelect)
    q8 = forms.ChoiceField(
        label="Dreams:How often do you dream?",
        choices=(('Vatta', 'I dream quite often, almost every night'),
                 ('Pitta', 'I dream occasionally but when I do, the dreams are vivid and bright'),
                 ('Kapha', 'I rarely dream and when I do, the dreams tend to be slow and detailed')),
        widget=forms.RadioSelect)
    q9 = forms.ChoiceField(
        label="Reaction:What is your first reaction to something new or strange?",
        choices=(('Vatta', 'Fear and worry. I go through elaborate scenarios in my head about what could happen'),
                 ('Pitta', 'Motivation; I am looking for ways to prove myself'),
                 ('Kapha', 'Reservation, I dont like change and would want to revert back to how things were')),
        widget=forms.RadioSelect)
    q10 = forms.ChoiceField(
        label="Leadership:How do you tend to interact with a team or a group of people?",
        choices=(('Vatta', 'I easily fit in with almost any group of people '),
                 ('Pitta', 'I am tough but fair. I have high expectations of people around me'),
                 ('Kapha', 'I treat my team like my family and like to connect at a personal level')),
        widget=forms.RadioSelect)
    q11 = forms.ChoiceField(
        label="Starting something new:How easily do you start something new?",
        choices=(('Vatta', 'I love starting new things and jump in with both feet'),
                 ('Pitta', 'I need to be convinced about starting something new first'),
                 ('Kapha', 'I like to plan everything in detail before I actually start')),
        widget=forms.RadioSelect)
    q12 = forms.ChoiceField(
        label="Planning: How do you usually like to make plans?",
        choices=(('Vatta', 'I like making open-ended plans and often figure things out along the way'),
                 ('Pitta', ' I like to be organized and structured in my planning'),
                 ('Kapha', 'I usually plan things out in great detail and like to take many opinions before I decide')),
        widget=forms.RadioSelect)


class PhysicalSurveyForm(forms.Form):
    '''
    feeling = forms.IntegerField(label='How are you feeling today?')
    stress = forms.IntegerField(label='On a scale of 1-10, how much stress are you feeling?')
    coping_mechanisms = forms.IntegerField(label='What coping mechanisms do you use to manage your mental health?')
    '''

    q1 = forms.ChoiceField(
        label="What is your diet like?",
        choices=(('Sattva', 'Vegetarian'), ('Rajas', 'Infrequent Non-Vegetarian'),
                 ('Tamas', 'Frequent Non-Vegetarian')),
        widget=forms.RadioSelect)
    q2 = forms.ChoiceField(
        label="Do you consume any drugs, alcohol, or stimulants?",
        choices=(('Sattva', 'Never'),
                 ('Rajas', 'Occasionally'),
                 ('Tamas', 'Frequently')),
        widget=forms.RadioSelect)
    q3 = forms.ChoiceField(
        label="Do you feel the urge to sleep?",
        choices=(('Sattva', 'Little'),
                 ('Rajas', 'Moderate'),
                 ('Tamas', 'High')),
        widget=forms.RadioSelect)
    q4 = forms.ChoiceField(
        label="What’re your sensory impressions like?",
        choices=(('Sattva', 'Calm, Pure'),
                 ('Rajas', 'Mixed'),
                 ('Tamas', 'Disturbed')),
        widget=forms.RadioSelect)
    q5 = forms.ChoiceField(
        label="How active are you sexually?",
        choices=(('Sattva', 'Low'),
                 ('Rajas', 'Moderate'),
                 ('Tamas', 'High')),
        widget=forms.RadioSelect)
    q6 = forms.ChoiceField(
        label="SHow is your control of sense?",
        choices=(('Sattva', 'Good'),
                 ('Rajas', 'Moderate'),
                 ('Tamas', 'Weak')),
        widget=forms.RadioSelect)
    q7 = forms.ChoiceField(
        label="What is your speech like?",
        choices=(('Sattva', 'Calm and peaceful'),
                 ('Rajas', 'Agitated'),
                 ('Tamas', 'Dull')),
        widget=forms.RadioSelect)
    q8 = forms.ChoiceField(
        label="What is your cleanliness level?",
        choices=(('Sattva', 'High'),
                 ('Rajas', 'Moderate'),
                 ('Tamas', 'Low')),
        widget=forms.RadioSelect)
    q9 = forms.ChoiceField(
        label="RWhat is your work like?",
        choices=(('Sattva', 'Selfless'),
                 ('Rajas', 'For Personal Goals'),
                 ('Tamas', 'Lazy')),
        widget=forms.RadioSelect)
    q10 = forms.ChoiceField(
        label="How frequently do you get angry?",
        choices=(('Sattva', 'Rarely'),
                 ('Rajas', 'Sometimes'),
                 ('Tamas', 'Frequently')),
        widget=forms.RadioSelect)
    q11 = forms.ChoiceField(
        label="How often do you fear something?",
        choices=(('Sattva', 'Rarely'),
                 ('Rajas', 'Sometimes'),
                 ('Tamas', 'Frequently')),
        widget=forms.RadioSelect)
    q12 = forms.ChoiceField(
        label="How much do you desire?",
        choices=(('Sattva', 'Little'),
                 ('Rajas', ' Some'),
                 ('Tamas', 'Much')),
        widget=forms.RadioSelect)
