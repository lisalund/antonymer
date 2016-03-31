from django import forms

class SomeForm(forms.Form):
    CHOICES = ((1,'1'),
               (2,'2'),
               (3,'3'),
               (4,'4'),
               (5,'5'),)
    picked = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
