from django.db import models

class Posts(models.Model):
    sn = models.AutoField(primary_key=True)
    title= models.CharField(max_length=250)
    author= models.CharField(max_length=100)
    content = models.TextField()
    slug= models.CharField(max_length=150)
    timestamps = models.DateTimeField(blank = True) 
    
    def __str__(self): #this is for define user name in databse every contact level
        return self.title + ' by '+ self.author


