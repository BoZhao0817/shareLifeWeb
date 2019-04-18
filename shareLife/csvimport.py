import csv

from django.contrib.auth.models import User

from shareLife.models import Post, Location
import time
import random



path = "./listings.csv"



with open(path, newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=',')

    i = 0
    for row in data:
        if i >= 10:
            break
        #user

        #print(row)
        name_ = row[21]
        #print (name_)
        tail = str(random.randint(1, 1000))
        user = User.objects.create_user(username = name_+tail, password='123456')
        loc = Location.objects.all().filter(row[43])
        print(loc)
        userid = User.objects.all().filter(username__istartswith= name_)
        P = Post(name = row[4],body= row[5],lodcation = loc,author = userid, latitude=row[50] , longitude= row[51])
        # P.save()
        i += 1
