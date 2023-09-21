from django.db import models

# Create your models here.


class Registation(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    age = models.IntegerField()
    password = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    course = models.CharField(max_length=100)


    def __str__(self):
        return self.name