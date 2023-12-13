from django.db import models

# Create your models here.
class User_table(models.Model):
    nam=models.CharField(max_length=100)
    cnum=models.CharField(max_length=100)
    eml=models.CharField(max_length=100)
    password=models.CharField(max_length=100,default='website')
    uname=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
   
    def __str__(self):
        return self.nam
    
class userupload(models.Model):
    usid=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    upload=models.FileField(upload_to="userupload")
    dt=models.DateField(auto_now=True)
    status=models.CharField(max_length=100)  
    
    def __str__(self):
        return self.usid
    
class uploadcount(models.Model):
    usid=models.CharField(max_length=100)
    count=models.CharField(max_length=100)
    
    def __str__(self):
        return self.count      
class usermax(models.Model):
    dt=models.DateField(auto_now=True)
    userid=models.CharField(max_length=100)
    usernameMax=models.CharField(max_length=100)
    
    def __str__(self):
        return self.usenameMax
        
