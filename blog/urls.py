from django.conf.urls import url

from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'blog.views.blog_index', name='blog_home'),
]