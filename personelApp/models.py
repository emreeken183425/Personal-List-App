from django.db import models

# Create your models here.
class Deparment(models.Model):
    name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Personel(models.Model):
    departmant=models.ForeignKey(Deparment,on_delete=models.SET_NULL, null=True,related_name=''  )    