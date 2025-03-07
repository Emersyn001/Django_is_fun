from django.db import models

# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phones = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    email = models.EmailField(null=True)