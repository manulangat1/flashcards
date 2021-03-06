from django.db import models

# Create your models here.
class BaseModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
class Category(models.Model):
    course =  models.CharField(max_length=39)

    def __str__(self):
        return self.course
class Card(BaseModel):
    course = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name='courses')
    title = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.title