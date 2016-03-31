from django import forms

class SomeForm(forms.Form):
    CHOICES = ((1,'Usla'),
               (2,'Dåliga'),
               (3,'Okej'),
               (4,'Rätt bra'),
               (5,'Jättebra'),)
    picked = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
