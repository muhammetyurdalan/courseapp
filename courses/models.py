from django.db import models
from datetime import datetime

# Create your models here..
class Course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    imageUrl=models.CharField(max_length=50)
    date=models.DateField(datetime.now())
    isActive=models.BooleanField()
    
    
    def __str__(self):
        return f"{self.title}"