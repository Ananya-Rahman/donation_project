from django.shortcuts import render
from .models import Donate

def donate(request):
    if request.method=='POST':
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        transaction_date = request.POST.get('transaction_date')
        donate_amount = request.POST.get('amount')
        phone_number = request.POST.get('phn_number')
        address = request.POST.get('address')
       
      
    
        donatedata = Donate(name = name, email = email, transaction_date= transaction_date, donate_amount =amount, phone_number=phn_number,address=address   )
        donatedata.save()   
    return render(request,'donate.html')
    