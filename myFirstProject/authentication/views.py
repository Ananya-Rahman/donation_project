from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

def authlogin(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username= name, password= password)
        
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.error(request, 'Username or password Invalid!')
               
    return render(request,'authentication/login.html')

def authregistration(request):
    if request.method == 'POST':
         username = request.POST['name']
         email = request.POST['email']
         password = request.POST['password']
         confirm_password = request.POST['confirm_password']
         
         if password == confirm_password:
             if User.objects.filter(username=username).exists():
                 messages.error(request,'Username Already Exists!')
             elif User.objects.filter(email=email).exists():
                 messages.error(request,'Email Already Exists!')   
             else:
                 
                user = User.objects.create_user(username=username, password=password, email = email)
                user.save()
                return redirect('login')
                
         else:
             messages.error(request, 'Password & confirm password not matched!')
             
    return render(request,'authentication/registration.html')

# def forgotpassword(request):
    
#     return render(request,'authentication/forgot.html')

# def PasswordResetDoneView(request):
    
#     return render(request,'authentication/password_reset_done.html')

# def PasswordResetConfirmView(request):
    
#     return render(request,'authentication/password_reset_confirm.html')

# def PasswordResetCompleteView(request):
    
#     return render(request,'authentication/password_reset_complete.html')


def userlogout(request):
   logout(request)
   messages.success(request, 'Successfully Logout!')
   return redirect('login') 