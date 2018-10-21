from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import HoodForm, HoodPostForm, CommentForm, BusinessForm, ProfileForm
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
			return redirect('home')

	else:
		form = HoodForm()
		return render(request,'hood/new_hood.html',{"form":form})

def GetHood(request):
	
	hoods = Neighbourhood.objects.filter(user = request.user)
	return render(request,'hood/hood.html',{"hoods":hoods})
    

@login_required(login_url='/accounts/login')
def profile(request):
    profile = UserProfile.objects.get(user=request.user)

    return render(request, 'profile.html', { 'profile':profile })

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
        
        return redirect('home')

def search(request):
    if request.GET['search']:
        search_term = request.GET.get('search')
        hoods = Neighbourhood.search_hood(search_term)
        message=f"{search_term}"
        return render(request, 'search.html', {'message':message, 'hoods':hoods})
    else:
        message = 'You have not searched for any neighbourhood'
        return render(request, 'search.html', {'message':message})


@login_required(login_url='/accounts/login')
def hoodPost(request):
	if Join.objects.filter(user_id=request.user).exists():
		if request.method == 'POST':
			form = HoodPostForm(request.POST)
			if form.is_valid():
				post = form.save(commit = False)
				post.user = request.user
				post.hood = request.user.join.hood_id
				post.save()
				return redirect('home')
		else:
			form = HoodPostForm()
			return render(request, 'hood/createpost.html', {'form':form })
	else:
		messages.error(request, 'Error! Cannot create Post')
		return render(request, 'home')

@login_required(login_url='/accounts/login')
def singlePost(request, postId):
	if Join.objects.filter(user_id = request.user).exists():
		post = Posts.objects.get(id = postId)
		comments = Comment.objects.filter(post = postId)
		if request.method == 'POST':
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.save(commit = False)
				comment.user = request.user
				comment.post = post
				comment.save()
				messages.success(request, 'You have made a comment successfully')
				return redirect('home')
		else:
			form = CommentForm()
		return render(request, 'hood/singlepost.html', {'post':post, 'form':form, 'comments':comments})
	else:
		messages.error(request, 'Join a neighbourhood to view post')
		return redirect('home')

@login_required(login_url='/accounts/login')
def allPosts(request):
	allPosts = Posts.objects.filter(user = request.user)
	return render(request, 'hood/posts.html', {'allPosts':allPosts})

@login_required(login_url='/accounts/login')
def getBusiness(request):
	business = Business.objects.filter(user =request.user)
	return  render(request, 'hood/business.html', {'business':business})


@login_required(login_url='/accounts/login')
def business(request):
	if Join.objects.filter(user_id = request.user).exists():
		if request.method == 'POST':
			form = BusinessForm(request.POST)
			if form.is_valid():
				business = form.save(commit= False)
				business.user = request.user
				business.hood = request.user.join.hood_id
				business.save()
				return redirect('business')
		else:
			form = BusinessForm()
			return render(request,'hood/createbiz.html', {'form':form})
	else:
		messages.error(request, 'Join a neighbourhood to view business')
		return redirect('home')

def search_business(request):
	if request.GET['searchBusiness']:
		search_term = request.GET.get('searchBusiness')
		business = Business.objects.filter(biz_name__icontains = search_term, hood = request.user.join.hood_id.id)
		message = f"{search_term}"
		return render(request, 'hood/bizsearch.html', {'message':message, 'business':business})
	else: 
		message = "Business not found"
		return render(request, 'hood/bizsearch.html', {'message':message})

@login_required(login_url='/accounts/login')
def editProfile(request):
	profile=UserProfile.objects.get(user=request.user)
	if request.method == 'POST':
		form = ProfileForm(request.POST,instance = profile)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = ProfileForm(instance=profile)
		return render(request, 'editprofile.html', {'form':form})

@login_required(login_url='/accounts/login')
def editBusiness(request,businessId):
	business = Business.objects.get(pk = businessId)
	if request.method == 'POST':
		form = BusinessForm(request.POST, instance = business)
		if form.is_valid():
			form.save()
			return redirect('business')
	else:
		form = BusinessForm(instance = business)
	return render(request, 'hood/editbiz.html', {'form':form, 'business':business})

@login_required(login_url='/accounts/login')
def deletePost(request, postId):
	Posts.objects.filter(pk = postId).delete()
	return render(request,'hood/my_hood.html')

@login_required(login_url='/accounts/login')
def deleteBusiness(request,businessId):
	Business.objects.filter(pk= businessId).delete()
	return render(request,'hood/my_hood.html')

@login_required(login_url='/accounts/login')
def deleteHood(request, hoodId):
	Neighbourhood.objects.filter(pk = hoodId).delete()
	return render(request, 'home.html')











