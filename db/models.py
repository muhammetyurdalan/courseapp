from django.db import models

# Create your models here.
class UserName(models.Model):
    username=models.CharField(unique=True,max_length=255)
    cid=models.CharField(max_length=15)
    
    

    def __str__(self):
        return f"{self.username}"

     
