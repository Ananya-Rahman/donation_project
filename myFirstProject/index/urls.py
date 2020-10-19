from django.urls import path
from.import views

urlpatterns = [
    path('',views.home, name='home'),
    path('details/<int:id>/',views.donation_details, name='donation_detail'),
   
    path('about/',views.about, name='about'),
   
    
]