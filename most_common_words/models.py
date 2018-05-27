from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from upload_file.models import Document

class UserProject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #, default=''
    name_project = models.ForeignKey(Document, on_delete=models.CASCADE)



class TopWords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')  #, default=''
    name_project = models.ForeignKey(Document, on_delete=models.CASCADE, default='')
    word_pl = models.CharField(max_length=255, blank=True)
    word_eng = models.CharField(max_length=255, blank=True)
    word_frequency = models.SmallIntegerField(default=0)
    level = models.SmallIntegerField(default=0)
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.word_eng

