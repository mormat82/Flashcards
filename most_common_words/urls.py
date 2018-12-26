from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from most_common_words.views import segregate, save_most_common_words

urlpatterns = [
    url(r'^$', save_most_common_words, name='save_most_common_words'),
    url(r'^segregate/$', segregate, name='segregate'),
    # url(r'^save-most-common-words/$', save_most_common_words, name='save_most_common_words'),
]