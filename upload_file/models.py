from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import os

class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # def filename(self):
    #     return os.path.basename(self.document.name)
    def __str__(self):
        return self.description
