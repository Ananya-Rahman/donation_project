from django.urls import path
from.import views

urlpatterns = [
    path('<int:id>/',views.index, name='index1'),
    path('charge/',views.charge, name='charge'),
    path('success/<str:args>/', views.successMsg, name='success'),
 
    
   
    
]