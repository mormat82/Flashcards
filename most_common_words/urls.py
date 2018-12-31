from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from most_common_words.views import segregate, save_most_common_words, delete_word, know_words

urlpatterns = [
    url(r'^$', save_most_common_words, name='save_most_common_words'),
    url(r'^segregate/$', segregate, name='segregate'),
    url(r'^delete-word/$', delete_word, name='delete_word'),
    url(r'^know-words/$', know_words, name='know_words'),
    # url(r'^save-most-common-words/$', save_most_common_words, name='save_most_common_words'),
]