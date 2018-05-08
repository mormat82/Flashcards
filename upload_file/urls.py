from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from upload_file.views import home, model_form_upload

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^uploads/form/$', model_form_upload, name='model_form_upload'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^frequently-words', )
]