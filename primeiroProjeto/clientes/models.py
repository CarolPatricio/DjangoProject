from django.db import models

class Person (models.Model):
    firs_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salario = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
