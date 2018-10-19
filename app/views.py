from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import HoodForm
from .models import Neighbourhood, Business, UserProfile, Join, Posts, Comment 


# Create your views here.
def home(request):

    if request.user.is_authenticated:
        if Join.objects.filter(user_id = request.user).exists():
            hood = Neighbourhood.objects.get(pk = request.user.join.hood_id.id)
            posts = Posts.objects.filter(hood = request.user.join.hood_id.id)
            business = Business.objects.filter(hood = request.user.join.hood_id.id)
            return render(request, 'hood/my_hood.html', {'hood':hood, 'business':business, 'posts':posts})
        else: 
            hoods = Neighbourhood.objects.all()
            return render(request, 'home.html', {'hoods':hoods})
    else:
        hoods = Neighbourhood.objects.all()
        return render(request, 'home.html', {'hoods':hoods})
        
@login_required(login_url='/accounts/login/')
def hood(request):
	'''
	This view function will create an instance of a neighbourhood
	'''
	if request.method == 'POST':
		form = HoodForm(request.POST)
		if form.is_valid():
			hood = form.save(commit = False)
			hood.user = request.user
			hood.save()
			messages.success(request, 'You Have succesfully created a hood.You may now join your neighbourhood')
			return redirect('hood/hood.html')

	else:
		form = HoodForm()
		return render(request,'hood/new_hood.html',{"form":form})

def GetHood(request):
	
	hoods = Neighbourhood.objects.filter(user = request.user)
	return render(request,'hood/hood.html',{"hoods":hoods})
    

@login_required(login_url='/accounts/login')
def profile(request):
    profile = UserProfile.objects.get(user=request.user)

    return render(request, 'profile/profile.html', { 'profile':profile })

@login_required(login_url='/accounts/login/')
def joinHood(request,hoodId):
	'''
	This view function will implement adding 
	'''
	neighbourhood = Neighbourhood.objects.get(pk = hoodId)
	if Join.objects.filter(user_id = request.user).exists():
		
		Join.objects.filter(user_id = request.user).update(hood_id = neighbourhood)
	else:
		
		Join(user_id=request.user,hood_id = neighbourhood).save()

	messages.success(request, 'Success! You have succesfully joined this Neighbourhood ')
	return redirect('home')

@login_required(login_url='/accounts/login/')
def exitHood(request,hoodId):
    if Join.objects.filter(user_id=request.user).exists():
        Join.objects.get(user_id=request.user).delete()
        messages.error(request, 'You have successfully exited this Neighbourhood')
        return redirect('home')
