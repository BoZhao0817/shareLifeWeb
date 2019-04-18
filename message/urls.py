from django.conf.urls import url

from . import views

app_name = 'message'
urlpatterns = [
    url(r'^message/'
        r'post/(?P<pk>[0-9]+)/$', views.detailPost, name='post_message'),
]