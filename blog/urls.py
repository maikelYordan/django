from django.conf.urls import url

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', "blog.views.blog_home", name='blog_home'),
]