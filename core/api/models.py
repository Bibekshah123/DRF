from django.db import models

# Create your models here.
class Sathi(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    college_name = models.CharField(max_length=100)
    location = models.CharField()
    nick_name = models.CharField(max_length=50)
    description = models.TextField()
    
    def __str__(self):
        return self.name