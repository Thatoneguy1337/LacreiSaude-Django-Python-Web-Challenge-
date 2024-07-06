from django.db import models

class Professionals():
        
    class Meta:
        ordering = ["id"]
    
    fullname = models.CharField(max_length=50, unique=True)
    profession = models.CharField(max_length=20)
    adress = models.CharField(max_length=120) 
    contact = models.CharField(max_length=80)
    socialname = models.CharField(max_length=50)
