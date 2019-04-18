# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime

DEFAULT_LOCATION_ID = 1

class Category(models.Model):
    name = models.CharField(max_length=100)


class Tag(models.Model):
    name = models.CharField(max_length=100)



class Location(models.Model):
    name = models.CharField(max_length=100,default="Chicago")

    def __str__(self):
        return '%s' % self.name


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


    def get_absolute_url(self):
        return reverse('single',
                       kwargs={'pk': self.pk})

    def __str__(self):
        return '%s' % self.name





class PostDetail(models.Model):

    property_id = models.AutoField(primary_key=True)
    property_size = models.CharField(max_length=70)
    bedrooms = models.CharField(max_length=200, blank=True)
    bathrooms = models.CharField(max_length=200, blank=True)
    garage_size = models.CharField(max_length=200, blank=True)
    year_built = models.CharField(max_length=70, blank=True)
    address = models.CharField(max_length=200, blank=True)
    price = models.CharField(max_length=70, blank=True)
    description = models.CharField(max_length=200, blank=True)
    name = models.ForeignKey(Post,on_delete=models.CASCADE,default=DEFAULT_LOCATION_ID)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=DEFAULT_LOCATION_ID)




    # def __str__(self):
    #     return '%s' % self.property_size,\
               # '%s' % self.property_size,\
               # '%s' % self.bedrooms,\
               # '%s' % self.bathrooms, \
               # '%s' % self.garage_size, \
               # '%s' % self.year_built, \
               # '%s' % self.address, \
               # '%s' % self.price, \
               # '%s' % self.description, \
               # '%s' % self.name,

    # class Meta:
    #     ordering = ['property_size']




# class Message(models.Model):
#     text = models.CharField(max_length=140)
#
#     sender = models.ForeignKey(User, on_delete = models.CASCADE)
#     receiver  = models.ForeignKey(User, on_delete = models.CASCADE)
#     time = models.DateTimeField()
# class Message(models.Model):
#     text = models.CharField(max_length=140)
#
#     sender = models.ForeignKey(User, on_delete = models.CASCADE)
#     receiver  = models.ForeignKey(User, on_delete = models.CASCADE)
#     time = models.DateTimeField()



