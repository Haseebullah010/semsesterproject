from django.db import models

# Create your models here.
class signup(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    name= models.CharField(max_length=100)
    number= models.CharField(max_length=100)
    mail= models.EmailField()
    password1= models.CharField(max_length=100 )
    
    def __str__(self):
        return str(self.id)


class signin(models.Model):
    
    name= models.CharField(max_length=100)
    password1= models.CharField(max_length=100)

    
    def __str__(self):
        return str(self.id)
