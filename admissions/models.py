from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=1000)
    fathername = models.CharField(max_length=1000)
    classname = models.IntegerField()
    contact = models.CharField(max_length=1000)

class Teacher(models.Model):
    name = models.CharField(max_length=1000)
    exp = models.IntegerField()
    subject = models.CharField(max_length=1000)
    contact = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('listteachers')
        #return reverse('getteacherinfo',kwargs = {'pk':self.pk})
