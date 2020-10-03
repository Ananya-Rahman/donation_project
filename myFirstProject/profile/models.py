from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email =models.TextField(max_length=100, blank=False)
    post_title =models.TextField(max_length=100, blank=False)
    post_description =models.TextField(max_length=700, blank=False)
   
    
    def __str__(self):
       return self.post_title
