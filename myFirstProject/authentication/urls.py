from django.urls import path
from.import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.authlogin, name='login'),
    path('registration/',views.authregistration, name='registration'),
    
#     path('forgot-password/',
#          auth_views.ForgotPasswordView.as_view(template_name="authentication/forgot.html"),
#          name='forgotpassword'),
#     path('password-reset/done/',
#          auth_views.PasswordResetDoneView.as_view(template_name="authentication/password_reset_done.html"),
#          name='password_reset_done'),
#     path('password-reset-confirm/<uidb64>/<token>/',
#          auth_views.PasswordResetConfirmView.as_view(template_name="authentication/password_reset_confirm.html"),
#          name='password_reset_confirm'),
#     path('password-reset-complete',
#          auth_views.PasswordResetCompleteView.as_view(template_name="authentication/password_reset_complete.html"),
#          name='password_reset_complete'),
    path('logout/',views.userlogout,name='logout'),
   
    
    
]