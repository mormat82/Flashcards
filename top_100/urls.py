from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from top_100.views import FlashcardsListView #CreateListFlashcards

urlpatterns = [

    # url(r'^(?P<book_id>(\d)+)/$', FlashcardsListView.as_view(), name='top_flascards'),
    url(r'^$', FlashcardsListView.as_view(), name='top_flascards'),
    # url(r'^create_list', CreateListFlashcards.as_view(), name='create_list'),

]