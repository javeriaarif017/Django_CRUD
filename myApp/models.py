from django.db import models
 
# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=50)
    name = models.CharField(max_length =20)
    email = models.EmailField()
    econtact = models.CharField(max_length=25)


    def __str__(self):
        return self.name


    





    
