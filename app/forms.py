from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Neighbourhood, Posts, Comment, Business, UserProfile

class HoodForm(forms.ModelForm):
    class Meta: 
        model = Neighbourhood
        fields = ['hood_name','hood_description', 'hood_location', 'hood_count']

class HoodPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['biz_name', 'biz_description', 'biz_email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['user_bio']