from django.db import models
from django.contrib.auth.models import User

class Library(models.Model):
    name = models.CharField(max_length=30,null = True)
    admin = models.OneToOneField(User, on_delete=models.CASCADE)

class Book(models.Model):
	bname = models.CharField(max_length=30,null = True)
	libery = models.ForeignKey(Library,on_delete=models.CASCADE,related_name='books')
	current_owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,related_name='books')