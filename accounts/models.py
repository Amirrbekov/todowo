from django.db import models

# Create your models here.

class Register(models.Model):

    fullname = models.CharField(max_length=100)
    username = models.CharField(max_length=25, unique= True)
    mail = models.EmailField(unique= True)
    password = models.CharField(max_length=25)
    confirm = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

class Login(models.Model):

    username = models.CharField(max_length = 25, unique = True)
    password = models.CharField(max_length = 25)

    def __str__(self):
        return self.username
