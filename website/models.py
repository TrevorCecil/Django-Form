from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    passwd= models.CharField(max_length=16)
    age = models.IntegerField(default=0, null=True,blank=True)

    def __str__(self):
        return self.fname + ' ' + self.lname