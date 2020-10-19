from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description =models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='about/', blank= False)
    
    def __str__(self):
       return self.title

class Slider(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description =models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='slider/', blank= False)
    
    def __str__(self):
       return self.title

class Donor(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField(upload_to='donor/', blank= False)
    
    def __str__(self):
       return self.name

class Donation(models.Model):
    image = models.ImageField(upload_to='donation/', blank= False)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=700, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    raised_amount= models.FloatField(null=True, blank=True) 
    goal_amount= models.FloatField(null=True, blank=True) 
    
    def __str__(self):
       return self.title
   