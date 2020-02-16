from django.db import models

# Create your models here.
class BaseModel(models.Model):
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
class Card(BaseModel):
    title = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.title