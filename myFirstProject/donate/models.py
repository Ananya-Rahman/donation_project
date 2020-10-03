from django.db import models


class Donate(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email =models.TextField(max_length=100, blank=False)
    transaction_date =models.DateField(null=True, blank=True)
    donate_amount= models.FloatField(null=True, blank=True) 
    phone_number =models.FloatField(null=True, blank=True) 
    address =models.TextField(max_length=100, blank=False) 
   
    
    
   
    
    def __str__(self):
       return self.name