from django.shortcuts import render
from .models import Profile
from django.contrib import messages

def profile(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        post_title = request.POST.get('post_title')
        post_description = request.POST.get('post_description')
        
        profiledata = Profile(name = name, email = email, post_title= post_title, post_description=post_description)
        profiledata.save()

    return render(request,'profile.html')
