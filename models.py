from django.db import models

# Create your models here.
class registers(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=70)
    