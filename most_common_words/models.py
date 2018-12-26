from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from upload_file.models import Document


class TopWords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    name_project = models.ForeignKey(Document, on_delete=models.CASCADE, default='')
    word_pl = models.CharField(max_length=255, blank=True)
    word_eng = models.CharField(max_length=255, blank=True)
    word_frequency = models.SmallIntegerField(default=0)
    level = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.word_eng


class Statistics(models.Model):
    name_project = models.ForeignKey(Document, on_delete=models.CASCADE, default='')
    total_amount_of_words = models.SmallIntegerField(default=0)
    amount_of_unique_words = models.SmallIntegerField(default=0)
    amount_of_unknown_words = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.total_amount_of_words