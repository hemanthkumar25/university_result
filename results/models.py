from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length = 20)  
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.id)+'-'+self.name+'-'+self.address+'-'+self.city+'-'+self.phone+'-'+self.email
