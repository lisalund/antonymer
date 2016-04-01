#!/usr/bin/python
# -*- coding: utf-8 -*-
from django import forms

class SomeForm(forms.Form):
    CHOICES = ((1,'Usel'),
               (2,'Dålig'),
               (3,'Okej'),
               (4,'Rätt bra'),
               (5,'Jättebra'),)
    svar = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
