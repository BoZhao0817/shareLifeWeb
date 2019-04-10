# Create your models here.
from django.db import models
from django.contrib.auth.models import User
import datetime

DEFAULT_LOCATION_ID = 1

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


class Message(models.Model):
    text = models.CharField(max_length=140)

    sender = models.ForeignKey(User, on_delete = models.CASCADE)
    receiver  = models.ForeignKey(User, on_delete = models.CASCADE)
    time = models.DateTimeField()



