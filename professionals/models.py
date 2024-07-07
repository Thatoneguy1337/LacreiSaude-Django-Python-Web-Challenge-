from django.db import models

class Professionals(models.Model):
    fullname = models.CharField(max_length=50, unique=True)
    profession = models.CharField(max_length=20)
    address = models.CharField(max_length=120)  
    contact = models.CharField(max_length=80)
    socialname = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.fullname


