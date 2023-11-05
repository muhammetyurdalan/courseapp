from django.db import models
from datetime import datetime
from django.utils.text import slugify

# Create your models here..
class Course(models.Model):
    title=models.CharField(max_length=50)
    description=models.TextField()
    imageUrl=models.CharField(max_length=50)
    date=models.DateField(datetime.now())
    isActive=models.BooleanField()
    slug=models.SlugField(default="",null=False,unique=True,db_index=True)
    isUptaded=models.BooleanField(default=True)
    
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super().save(args,kwargs)
    
    
    def __str__(self):
        return f"{self.title}"
    
class Categories(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    slug=models.SlugField()