from django.db import models
from index.models import Donation 
# Create your models here.



class Payment(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email =models.TextField(max_length=100, blank=False)
    transaction_date =models.DateField(null=True, blank=True)
    donate_amount= models.FloatField(null=True, blank=True) 
    phone_number =models.FloatField(null=True, blank=True) 
    address =models.TextField(max_length=100, blank=False) 
    donate  = models.ForeignKey(Donation, on_delete=models.CASCADE,null=True, blank=True)
    
    
   
    
    def __str__(self):
       return self.name