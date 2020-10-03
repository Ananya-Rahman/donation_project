from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from .models import Payment

import stripe

stripe.api_key = "sk_test_51HWpI3JivNz55t0OWKWCnL6KcQdhzGk2PcXda9bhvr691cbNd5F1xyu1Klef7PdFivEjnvGL6cv7tUOszGHWIhWP00STDM8ty3"

def index(request):
    return render(request, 'payment/index1.html')

def charge(request):
    
   
    if request.method == 'POST':
        print('Data:', request.POST)
        
        amount = int(request.POST['amount'])
        
        customer = stripe.Customer.create(
            email = request.POST['email'],
            name = request.POST['nickname'],
            source = request.POST['stripeToken']
        )
        charge = stripe.Charge.create(
            customer =customer,
            amount=amount*100,
            currency= 'usd',
            description = "Donation"
        )
        if request.method=='POST':
            email = request.POST['email']
            name = request.POST['nickname']
            donate_amount= amount
            transaction_date= request.POST['stripeToken'] 
             
               
        
        
   
        paymentdata=Payment(name= name, email=email,donate_amount= donate_amount)
        paymentdata.save()
    return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
    amount = args 
    return render(request, 'payment/success.html', {'amount':amount})