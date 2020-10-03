from django.shortcuts import render
from .models import Contact
from django.contrib import messages


def contact(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
   
        contactdata=Contact(name= name, email=email, message=message)
        contactdata.save()
        

            
    return render(request,'contact.html')