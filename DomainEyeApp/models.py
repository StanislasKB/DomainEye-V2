from django.db import models

class History(models.Model):
    domain=models.CharField(max_length=255)
    temps= models.DateTimeField(auto_now=False, auto_now_add=True)
   
