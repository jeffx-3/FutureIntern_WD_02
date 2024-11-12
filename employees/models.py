from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    contact = models.CharField(max_length=25)
    employment_type = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
    hired = models.DateField(null=True)
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.name
    

    