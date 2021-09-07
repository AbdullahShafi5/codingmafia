from django.db import models

class Contact(models.Model):
    sn = models.AutoField(primary_key=True)
    name= models.CharField(max_length=225)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=70)
    content = models.TextField()
    timestamps = models.DateTimeField(auto_now_add=True, blank = True) 
    def __str__(self): #this is for define user name in databse contact every level
        return "This shit is from " + self.name +'-' + self.email
     

class SubscribeEmail(models.Model):
    sbscrb_email  = models.EmailField()