from django.db import models

# Create your models here.

class Student(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    reg_no = models.IntegerField()
    grade = models.CharField(max_length=2)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, default='Unknown Address')
    email = models.EmailField(unique=True, null=True, blank=True)
    parent_phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
