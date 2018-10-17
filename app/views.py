from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            return HttpResponse('accounts/login')
    else:
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {'form':form})



@login_required(login_url='/')
def home(request):

    return render(request, 'home.html')
