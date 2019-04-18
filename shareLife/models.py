# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import  reverse
import datetime

DEFAULT_LOCATION_ID = 1
DEFAULT_POST_ID =1
DEFAULT_USER_ID =1

class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)



class Location(models.Model):
    name = models.CharField(max_length=100,default="Chicago")

    def __str__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=70)

    body = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    excerpt = models.CharField(max_length=200, blank=True)

    location = models.ForeignKey(Location,on_delete=models.CASCADE,default=DEFAULT_LOCATION_ID)
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User,on_delete=models.CASCADE)

    address = models.CharField(max_length=200, blank=True)
    startDate = models.DateField(default=datetime.date.today)
    endDate = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.name

    def get_absolute_url(self):git
        return reverse('shareLife:post_detail', kwargs={'pk': self.pk})







