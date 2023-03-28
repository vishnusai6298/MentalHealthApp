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


class PhysicalDoshaSurveyForm(forms.Form):
    '''
    feeling = forms.IntegerField(label='How are you feeling today?')
    stress = forms.IntegerField(label='On a scale of 1-10, how much stress are you feeling?')
    coping_mechanisms = forms.IntegerField(label='What coping mechanisms do you use to manage your mental health?')
    '''

    q1 = forms.ChoiceField(
        label="What is your body frame like?",
        choices=(
            ('Vatta', 'Tall or short, thin. Poorly developed physique'),
            ('Pitta', 'Medium. Moderately developed physique'),
            ('Kapha', 'Stout, stocky, short. Well Developed physique')
        ),
        widget=forms.RadioSelect
    )

    q2 = forms.ChoiceField(
        label="What is your weight like?",
        choices=(
            ('Vatta', 'Low, hard-to-hold weight, prominent veins, and bones'),
            ('Pitta', 'Moderate, good muscles'),
            ('Kapha', 'Heavy, tends towards obesity')
        ),
        widget=forms.RadioSelect
    )

    q3 = forms.ChoiceField(
        label="What is your complexion like?",
        choices=(
            ('Vatta', 'Dull, brown, darkish'),
            ('Pitta', 'Red, ruddy, flushed, glowing'),
            ('Kapha', 'White, pale')
        ),
        widget=forms.RadioSelect
    )

    q4 = forms.ChoiceField(
        label="How are your skin texture and temperature?",
        choices=(
            ('Vatta', 'Thin, dry, cold, rough, cracked, prominent veins'),
            ('Pitta', 'Warm, moist, pink, with moles, freckles, acne'),
            ('Kapha', 'Thick, white, moist, cold, soft, smooth')
        ),
        widget=forms.RadioSelect
    )

    q5 = forms.ChoiceField(
        label="What’s your hair like?",
        choices=(
            ('Vatta', 'Scanty, coarse, dry, brown, slightly wavy'),
            ('Pitta', 'Moderate, fine, soft, early gray or bald'),
            ('Kapha', 'Abundant, oily, thick, very wavy, lustrous')
        ),
        widget=forms.RadioSelect
    )

    q6 = forms.ChoiceField(
        label="What’s your head like?",
        choices=(
            ('Vatta', 'Small, thin, long, unsteady'),
            ('Pitta', 'Moderate'),
            ('Kapha', 'Large, Stocky, steady')
        ),
        widget=forms.RadioSelect
    )

    q7 = forms.ChoiceField(
        label="What’s your forehead like?",
        choices=(
            ('Vatta', 'Small, wrinkled'),
            ('Pitta', 'Moderate, with folds'),
            ('Kapha', 'Large, broad')
        ),
        widget=forms.RadioSelect
    )

    q8 = forms.ChoiceField(
        label="What’s your face like?",
        choices=(
            ('Vatta', 'Thin, small, long, wrinkled, dusky, dull'),
            ('Pitta', 'Moderate, ruddy, sharp, contours'),
            ('Kapha', 'Large, round, fat, while or pale, soft contours')
        ),
        widget=forms.RadioSelect
    )

    q9 = forms.ChoiceField(
        label="What’s your neck like?",
        choices=(
            ('Vatta', 'Thin, long'),
            ('Pitta', 'Medium'),
            ('Kapha', 'Large, thick')
        ),
        widget=forms.RadioSelect
    )

    q10 = forms.ChoiceField(
        label="What are your eyebrows like?",
        choices=(
            ('Vatta', 'Small, thin, unsteady'),
            ('Pitta', 'Moderate, fine'),
            ('Kapha', 'Thick, bushy, many hairs')
        ),
        widget=forms.RadioSelect
    )

    q11 = forms.ChoiceField(
        label="What are your eyelashes like?",
        choices=(
            ('Vatta', 'Small, dry, firm'),
            ('Pitta', 'Small, thin, fine'),
            ('Kapha', 'Large, thick, oily, firm')
        ),
        widget=forms.RadioSelect
    )

    q12 = forms.ChoiceField(
        label="What are your eyes like?",
        choices=(
            ('Vatta', 'Small, dry, thin, brown, dull, unsteady'),
            ('Pitta', 'Medium, thin, red (inflamed easily), green, piercing'),
            ('Kapha', 'Wide, prominent, thick, oily, white, attractive')
        ),
        widget=forms.RadioSelect
    )

    q13 = forms.ChoiceField(
        label="What is your nose like?",
        choices=(
            ('Vatta', 'Thin, small, long, dry, cooked'),
            ('Pitta', 'Medium'),
            ('Kapha', 'Thick, big, firm, oily')
        ),
        widget=forms.RadioSelect
    )

    q14 = forms.ChoiceField(
        label="What are your lips like?",
        choices=(
            ('Vatta', 'Thin, small, darkish, dry, unsteady'),
            ('Pitta', 'Medium, soft, red'),
            ('Kapha', 'Thick, large, oily, smooth, firm')
        ),
        widget=forms.RadioSelect
    )

    q15 = forms.ChoiceField(
        label="How are your teeth & Gums?",
        choices=(
            ('Vatta', 'Thin, dry, small, rough, crooked, receding gums'),
            ('Pitta', 'Medium, soft, pink, gums bleed easily'),
            ('Kapha', 'Large, thick, soft, pink, oily')
        ),
        widget=forms.RadioSelect
    )

    q16 = forms.ChoiceField(
        label="What are you shoulders like?",
        choices=(
            ('Vatta', 'Thin, small, flat, hunched'),
            ('Pitta', 'Medium'),
            ('Kapha', 'Broad, thick, firm, oily')
        ),
        widget=forms.RadioSelect
    )

    q17 = forms.ChoiceField(
        label="What is your chest like?",
        choices=(
            ('Vatta', 'Thin, small, narrow, poorly developed'),
            ('Pitta', 'Medium'),
            ('Kapha', 'Broad, large, well or overly developed')
        ),
        widget=forms.RadioSelect
    )

    q18 = forms.ChoiceField(
        label="What are your arms like?",
        choices=(
            ('Vatta', 'Thin, overly small or long, poorly developed'),
            ('Pitta', 'Medium'),
            ('Kapha', 'Large, thick, round, well-developed')
        ),
        widget=forms.RadioSelect
    )

    q19 = forms.ChoiceField(
        label="What are your hands like?",
        choices=(
            ('Vatta', 'Small, thin, dry, cold, rough, fissured, unsteady'),
            ('Pitta', 'Medium, warm, pink'),
            ('Kapha', 'Large, thick, oily, cool, firm')
        ),
        widget=forms.RadioSelect
    )

    q20 = forms.ChoiceField(
        label="What are your thighs like?",
        choices=(
            ('Vatta', 'Thin, narrow'),
            ('Pitta', 'Medium'),
            ('Kapha', 'Well-developed, rounded, fat')
        ),
        widget=forms.RadioSelect
    )

    q21 = forms.ChoiceField(
        label="What are your legs like?",
        choices=(
            ('Vatta', 'Thin, excessively long or short, prominent knees'),
            ('Pitta', 'Medium'),
            ('Kapha', 'Large, Stocky')
        ),
        widget=forms.RadioSelect
    )

    q22 = forms.ChoiceField(
        label="What are your calves like?",
        choices=(
            ('Vatta', 'Small, hard, tight'),
            ('Pitta', 'Loose, soft'),
            ('Kapha', 'Shapely, firm')
        ),
        widget=forms.RadioSelect
    )

    q23 = forms.ChoiceField(
        label="What are your feet like?",
        choices=(
            ('Vatta', 'Small, thin, long, dry, rough, fissured, unsteady'),
            ('Pitta', 'Medium, soft, pink'),
            ('Kapha', 'Large, thick, hard, firm')
        ),
        widget=forms.RadioSelect
    )

    q24 = forms.ChoiceField(
        label="What are your joints like?",
        choices=(
            ('Vatta', 'Small, thin, dry, unsteady, cracking'),
            ('Pitta', 'Medium, soft, loose'),
            ('Kapha', 'Large, thick, well built')
        ),
        widget=forms.RadioSelect
    )

    q25 = forms.ChoiceField(
        label="What are your nails like?",
        choices=(
            ('Vatta', 'Small, thin, dry, rough, fissured, cracked, darkish'),
            ('Pitta', 'Medium, soft, pink'),
            ('Kapha', 'Large, thick, smooth, white, firm, oily')
        ),
        widget=forms.RadioSelect
    )

    q26 = forms.ChoiceField(
        label="Which of the following best describes your urine?",
        choices=(
            ('Vatta', 'Scanty, difficult, color-less'),
            ('Pitta', 'Profuse, yellow, red, burning'),
            ('Kapha', 'Moderate, whitish, milky')
        ),
        widget=forms.RadioSelect
    )

    q27 = forms.ChoiceField(
        label="Which of the following best describes your feces?",
        choices=(
            ('Vatta', 'Scanty, dry, hard, difficult or painful, gas, tends towards constipation'),
            ('Pitta', 'Abundant, loose, yellowish, tends to diarrhea, with burning sensation'),
            ('Kapha', 'Moderate, solid, sometimes pale in color, mucus in stool')
        ),
        widget=forms.RadioSelect
    )

    q28 = forms.ChoiceField(
        label="Which of the following best describes your sweat/body odor?",
        choices=(
            ('Vatta', 'Scanty, no smell'),
            ('Pitta', 'Profuse, hot, strong smell'),
            ('Kapha', 'Moderate, cold, pleasant smell')
        ),
        widget=forms.RadioSelect
    )

    q29 = forms.ChoiceField(
        label="Which of the following best describes your appetite?",
        choices=(
            ('Vatta', 'Variable, erratic'),
            ('Pitta', 'Strong, sharp'),
            ('Kapha', 'Constant, low')
        ),
        widget=forms.RadioSelect
    )

    q30 = forms.ChoiceField(
        label="Which of the following best describes your taste preferences?",
        choices=(
            ('Vatta', 'Prefers sweet, sour, or salty food, cooked with oil and spiced'),
            ('Pitta', 'Prefers sweet, bitter or astringent food, raw, lightly cooked without spices or extra salt'),
            ('Kapha', 'Prefers pungent, bitter or astringent food, cooked with spices but not oil')
        ),
        widget=forms.RadioSelect
    )

    q31 = forms.ChoiceField(
        label="Which of the following best describes your circulation?",
        choices=(
            ('Vatta', 'Poor, variable, erratic'),
            ('Pitta', 'Good, warm'),
            ('Kapha', 'Slow, steady')
        ),
        widget=forms.RadioSelect
    )
    q32 = forms.ChoiceField(
        label="Which of the following best describes your activity?",
        choices=(
            ('Vatta', 'Quick, fast, unsteady, erratic, hyperactive'),
            ('Pitta', 'Medium, motivated, purposeful, goal seeking'),
            ('Kapha', 'Slow, steady, stately')
        ),
        widget=forms.RadioSelect
    )

    q33 = forms.ChoiceField(
        label="Which of the following best describes your strength/endurance?",
        choices=(
            ('Vatta', 'Low, poor endurance, starts and stops quickly'),
            ('Pitta', 'Medium, intolerant of heat'),
            ('Kapha', 'Strong, good endurance, but slow in starting')
        ),
        widget=forms.RadioSelect
    )

    q34 = forms.ChoiceField(
        label="Which of the following best describes your sexual nature?",
        choices=(
            ('Vatta', 'Variable, erratic, deviant, strong desire but low energy, few children'),
            ('Pitta', 'Moderate, passionate, quarrelsome, dominating'),
            ('Kapha', 'Low but constant sexual desire, good sexual energy, devoted, many children')
        ),
        widget=forms.RadioSelect
    )

    q35 = forms.ChoiceField(
        label="Which of the following best describes your sensitivity?",
        choices=(
            ('Vatta', 'Fear of cold, wind, sensitive to dryness'),
            ('Pitta', 'Fear of heat, dislike of sun, fire'),
            ('Kapha', 'Fear of cold, damp, likes wind and sun')
        ),
        widget=forms.RadioSelect
    )

    q36 = forms.ChoiceField(
        label="Which of the following best describes your resistance to disease?",
        choices=(
            ('Vatta', 'Poor, variable, weak immune system'),
            ('Pitta', 'Medium, prone to infection'),
            ('Kapha', 'Good, prone to congestive disorders')
        ),
        widget=forms.RadioSelect
    )

    q37 = forms.ChoiceField(
        label="Which of the following best describes your disease tendency?",
        choices=(
            ('Vatta', 'Nervous system diseases, pain, arthritis, mental disorders'),
            ('Pitta', 'Fevers, infections, inflammatory diseases'),
            ('Kapha', 'Respiratory system diseases, mucus, edema')
        ),
        widget=forms.RadioSelect
    )

    q38 = forms.ChoiceField(
        label="What is your reaction to medications?",
        choices=(
            ('Vatta', 'Quick, low dosage needed, unexpected side effects or nervous reactions'),
            ('Pitta', 'Medium, average dosage'),
            ('Kapha', 'Slow, high dosage required, effects slow to manifest')
        ),
        widget=forms.RadioSelect
    )

    q39 = forms.ChoiceField(
        label="How is your pulse?",
        choices=(
            ('Vatta', 'Thready, rapid, superficial, irregular, weak; like a snake'),
            ('Pitta', 'Wiry, bounding, moderate; like a frog'),
            ('Kapha', 'Deep, slow, steady, rolling, slippery; like a swan')
        ),
        widget=forms.RadioSelect
    )
    q39 = forms.ChoiceField(
        label="How is your pulse?",
        choices=(
            ('Vatta', 'Thready, rapid, superficial, irregular, weak; like a snake'),
            ('Pitta', 'Wiry, bounding, moderate; like a frog'),
            ('Kapha', 'Deep, slow, steady, rolling, slippery; like a swan')
        ),
        widget=forms.RadioSelect
    )

    q40 = forms.ChoiceField(
        label="How is your voice?",
        choices=(
            ('Vatta', 'Low, weak, hoarse'),
            ('Pitta', 'High pitch, sharp'),
            ('Kapha', 'Pleasant, deep, good tone')
        ),
        widget=forms.RadioSelect
    )

    q41 = forms.ChoiceField(
        label="How is your speech?",
        choices=(
            ('Vatta', 'Quick, inconsistent, erratic, talkative'),
            ('Pitta', 'Moderate, argumentative, convincing'),
            ('Kapha', 'Slow, definite, not talkative')
        ),
        widget=forms.RadioSelect
    )

    q42 = forms.ChoiceField(
        label="Which of the following best describes your mental nature?",
        choices=(
            ('Vatta', 'Quick, adaptable, indecisive'),
            ('Pitta', 'Intelligent, penetrative, critical'),
            ('Kapha', 'Slow, steady dull')
        ),
        widget=forms.RadioSelect
    )

    q43 = forms.ChoiceField(
        label="How is your memory?",
        choices=(
            ('Vatta', 'Poor, notices things easily but forgets'),
            ('Pitta', 'Sharp, clear'),
            ('Kapha', 'Slow to take notice but will not forget')
        ),
        widget=forms.RadioSelect
    )

    q44 = forms.ChoiceField(
        label="What are your finances like?",
        choices=(
            ('Vatta', 'Earns and spends quickly, erratically'),
            ('Pitta', 'Spends on specific goals, causes or projects'),
            ('Kapha', 'Holds on to what one earns, particularly property')
        ),
        widget=forms.RadioSelect
    )

    q45 = forms.ChoiceField(
        label="Which of the following best describes your emotional tendencies?",
        choices=(
            ('Vatta', 'Fearly, anxious, nervous'),
            ('Pitta', 'Angry, irritable, contentious'),
            ('Kapha', 'Calm, content, attached, sentimental')
        ),
        widget=forms.RadioSelect
    )

    q46 = forms.ChoiceField(
        label="What are your neurotic tendencies?",
        choices=(
            ('Vatta', 'Hysteria, trembling, anxiety attacks'),
            ('Pitta', 'Extreme temper, rage, tantrums'),
            ('Kapha', 'Depressions, unresponsiveness, sorrow')
        ),
        widget=forms.RadioSelect
    )

    q47 = forms.ChoiceField(
        label="How is your faith?",
        choices=(
            ('Vatta', 'Erratic, changeable, rebel'),
            ('Pitta', 'Determined, fanatic, leader'),
            ('Kapha', 'Constant, loyal, conservative')
        ),
        widget=forms.RadioSelect
    )

    q48 = forms.ChoiceField(
        label="What is your sleep like?",
        choices=(
            ('Vatta', 'Light, tends towards insomnia'),
            ('Pitta', 'Moderate, may wake up but will fall asleep again'),
            ('Kapha', 'Heavy, difficulty in waking up')
        ),
        widget=forms.RadioSelect
    )

    q49 = forms.ChoiceField(
        label="What are your dreams like?",
        choices=(
            ('Vatta', 'Flying, moving, restless, nightmares'),
            ('Pitta', 'Colorful, passionate, conflict'),
            ('Kapha', 'Romantic, sentimental, watery, few dreams')
        ),
        widget=forms.RadioSelect
    )

    q50 = forms.ChoiceField(
        label="What are your habits?",
        choices=(
            ('Vatta', 'Likes speed, traveling, parks, plays, jokes, stories, trivia, artistic activities, dancing'),
            ('Pitta', 'Likes competitive sports, debates, politics, hunting, research'),
            ('Kapha', 'Likes water, sailing, flowers, cosmetics, business ventures, cooking')
        ),
        widget=forms.RadioSelect
    )


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
    q13 = forms.ChoiceField(
        label="How much pride do you have?",
        choices=(('Sattva', 'Modest'),
                 ('Rajas', ' Some Ego'),
                 ('Tamas', 'Vain')),
        widget=forms.RadioSelect)
    q14 = forms.ChoiceField(
        label="Do you face depression?",
        choices=(('Sattva', 'Never'),
                 ('Rajas', ' Sometimes'),
                 ('Tamas', 'Frequently')),
        widget=forms.RadioSelect)
    q15 = forms.ChoiceField(
        label="What do you feel about love?",
        choices=(('Sattva', 'Universal'),
                 ('Rajas', ' Personal'),
                 ('Tamas', 'Lacking in love')),
        widget=forms.RadioSelect)
    q16 = forms.ChoiceField(
        label="Do you display violent behavior?",
        choices=(('Sattva', 'Never'),
                 ('Rajas', ' Sometimes'),
                 ('Tamas', 'Frequently')),
        widget=forms.RadioSelect)
    q17 = forms.ChoiceField(
        label=" Do you have an attachment to money?",
        choices=(('Sattva', 'Little'),
                 ('Rajas', ' Some'),
                 ('Tamas', 'A Lot')),
        widget=forms.RadioSelect)
    q18 = forms.ChoiceField(
        label="Are you content?",
        choices=(('Sattva', 'Usually'),
                 ('Rajas', ' Partly'),
                 ('Tamas', 'Never')),
        widget=forms.RadioSelect)
    q19 = forms.ChoiceField(
        label="Are you someone who",
        choices=(('Sattva', 'Forgives easily'),
                 ('Rajas', ' Forgives with effort'),
                 ('Tamas', 'Holds long-term grudges')),
        widget=forms.RadioSelect)
    q20 = forms.ChoiceField(
        label="What's your concentration like?",
        choices=(('Sattva', 'Good'),
                 ('Rajas', ' Moderate'),
                 ('Tamas', 'Poor')),
        widget=forms.RadioSelect)
    q21 = forms.ChoiceField(
        label="What is your memory like?",
        choices=(('Sattva', 'Good'),
                 ('Rajas', ' Moderate'),
                 ('Tamas', 'Poor')),
        widget=forms.RadioSelect)
    q22 = forms.ChoiceField(
        label=" What’s your willpower like?",
        choices=(('Sattva', 'Strong'),
                 ('Rajas', ' Variable'),
                 ('Tamas', 'Weak')),
        widget=forms.RadioSelect)
    q23 = forms.ChoiceField(
        label="How truthful are you?",
        choices=(('Sattva', 'Always'),
                 ('Rajas', ' Most of the Time'),
                 ('Tamas', 'Rarely')),
        widget=forms.RadioSelect)
    q24 = forms.ChoiceField(
        label="HHow honest are you?",
        choices=(('Sattva', 'Always'),
                 ('Rajas', ' Most of the time'),
                 ('Tamas', 'Rarely')),
        widget=forms.RadioSelect)
    q25 = forms.ChoiceField(
        label="Do you feel peace of mind?",
        choices=(('Sattva', 'Generally'),
                 ('Rajas', ' Partly'),
                 ('Tamas', 'Rarely')),
        widget=forms.RadioSelect)
    q26 = forms.ChoiceField(
        label="How’s your creativity?",
        choices=(('Sattva', 'High'),
                 ('Rajas', ' Moderate'),
                 ('Tamas', 'Low')),
        widget=forms.RadioSelect)
    q27 = forms.ChoiceField(
        label="Do you indulge in spiritual study?",
        choices=(('Sattva', 'Daily'),
                 ('Rajas', ' Occasionally'),
                 ('Tamas', 'Never')),
        widget=forms.RadioSelect)
    q28 = forms.ChoiceField(
        label="Do you indulge in mantras and prayers?",
        choices=(('Sattva', 'Daily'),
                 ('Rajas', ' Occasionally'),
                 ('Tamas', 'Never')),
        widget=forms.RadioSelect)
    q29 = forms.ChoiceField(
        label="Do you meditate?",
        choices=(('Sattva', 'Daily'),
                 ('Rajas', ' Occasionally'),
                 ('Tamas', 'Never')),
        widget=forms.RadioSelect)
    q30 = forms.ChoiceField(
        label=" Do you perform acts of service?",
        choices=(('Sattva', 'Many'),
                 ('Rajas', ' Some'),
                 ('Tamas', 'None')),
        widget=forms.RadioSelect)
