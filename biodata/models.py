from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    reg_no = models.IntegerField()
    grade = models.CharField(max_length=2)
