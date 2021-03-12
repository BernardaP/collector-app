from django import forms
from .models import Feeding, Mogwai

class MogwaiForm(forms.ModelForm):
    class Meta:
        model = Mogwai
        fields = ['name', 'character', 'description', 'age']

class FeedingForm(forms.ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'time', 'meal']