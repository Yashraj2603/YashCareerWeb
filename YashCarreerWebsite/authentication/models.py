from django.db import models

# Create your models here.

class Signup(models.Model):
    First_name = models.CharField(max_length=20)
    Last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=40)
    Email_id = models.EmailField()
    pass1 = models.CharField(max_length=30)



