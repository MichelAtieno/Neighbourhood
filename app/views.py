from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import RegistrationForm
from .models import UserProfile


# Create your views here.
def home(request):
    
    return render(request, 'home.html')
    

@login_required(login_url='/accounts/login')
def profile(request):
    profile = UserProfile.objects.get(user=request.user)

    return render(request, 'profile/profile.html', { 'profile':profile })

