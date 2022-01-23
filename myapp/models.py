from tkinter import CASCADE
from unicodedata import name
from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name=models.CharField(max_length=100,null=False)
    last_name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=CASCADE)
    salary = models.IntegerField()
    bonus = models.IntegerField()
    role = models.ForeignKey(Role,on_delete=CASCADE)
    phone = models.IntegerField()

    def __str__(self):
        return self.first_name