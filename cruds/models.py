from django.db import models


# Create your models here.

class Profile(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField(max_length=25)
    Age = models.IntegerField(null=True, blank=True)
    Image = models.ImageField(upload_to='Prof_pic/', default='def.png')
    Address = models.TextField(max_length=50, null=True, blank=True)
    Phone_Number = models.TextField(max_length=15, null=True, blank=True)
    Date_Of_Birth = models.TextField(max_length=25, null=True, blank=True)
    Gender = models.TextField(max_length=8, null=True, blank=True)
    Religion = models.TextField(max_length=8, null=True, blank=True)


    def __str__(self):
        return str(self.Name)
