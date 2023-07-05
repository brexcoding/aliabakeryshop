from django.db import models

# items posting / items_function 
class Order(models.Model):
    name = models.CharField(max_length=44,blank=False ,default="", null= False)
    phone = models.CharField(blank=False ,default="" , null   = False , max_length=10)
    adress = models.CharField(max_length=50,blank=False ,default="" ,null = False)
    store_name = models.CharField(max_length=50,blank=False ,default="", null = False)
    quantity = models.CharField(default='1', null = True ,blank = True , max_length=5 )
   
    def __str__(self) : 
        return self.name 
    


