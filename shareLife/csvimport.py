import csv

from django.contrib.auth.models import User

from shareLife.models import Post, Location
import time
import random



city_dict = {"2":"boston", "3":"nyc", "4":"la", "5":"sf", "6":"seattle","7":'austin'}
for key, value in city_dict.items():
    path = "../data/"+ value +".csv"
    with open(path, newline='') as csvfile:
        data = csv.reader(csvfile, delimiter=',')
        i = 0
        for row in data:
            if i > 100:
                break
            #user
            #print(row)
            name_ = row[21]
            print (name_)
            tail = str(random.randint(1, 100000))
            user = User.objects.create_user(username = name_+tail, password='123456')
            user.save()

            loc = Location.objects.get(pk = key)
            userid = User.objects.get(username = name_ + tail)

            print(userid)
            P = Post(name = row[4],body= row[5],location = loc,author = userid, latitude=row[48] , longitude= row[49], pic_url=row[17], bedrooms = row[55], bathrooms = row[54])
            P.save()
            i += 1

