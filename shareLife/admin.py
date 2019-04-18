from django.contrib import admin

# Register your models here.
from shareLife.models import Category, Tag, Location, Post

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Location)
admin.site.register(Post)

