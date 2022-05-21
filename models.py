from django.db import models
from django import forms  

# Create your models here.
class customer(models.Model):
    #id=models.IntegerField()
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=15)
    def __str__(self):  #Mandatory Field
        return self.name
    
    


        
            
class Employee(models.Model):
    #id=models.IntegerField()
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    age=models.IntegerField()
    city=models.CharField(max_length=20)
    salary=models.IntegerField()
    designation=models.CharField(max_length=20)
    def __str__(self):  #Mandatory Field
        return self.name
    
    

        
        
        
        
        