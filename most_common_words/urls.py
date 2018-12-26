from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from most_common_words.views import segregate

urlpatterns = [
    # url(r'^$', most_used_words, name='most_used_words'),
    url(r'^segregate/$', segregate, name='segregate'),
]