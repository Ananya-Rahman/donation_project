from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from django.http import HttpResponse
from .models import About
from .models import Slider
from .models import Donor
from .models import Donation

def home(request):
    aboutdata = About.objects.all()[0]
    sliderdata = Slider.objects.all()
    donordata = Donor.objects.all()
    donationdata = Donation.objects.order_by("-created")
    
    context={
        'About': aboutdata,
        'Slider': sliderdata,
        'Donor' : donordata,
        'Donations': donationdata
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def donation_details(request,id):
    donation = Donation.objects.get(id=id) #first_id is donation table id second id is what i passed from details page
    return render(request,'donation_details.html',{"donation":donation})


# def contact(request):
#     return render(request,'contact.html')


