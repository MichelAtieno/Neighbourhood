from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighbourhood

class HoodForm(forms.ModelForm):
    class Meta: 
        model = Neighbourhood
        fields = ['hood_name','hood_description', 'hood_location', 'hood_count']
