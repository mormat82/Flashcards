# Generated by Django 2.0.2 on 2018-05-28 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('most_common_words', '0004_auto_20180527_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userproject',
            name='name_project',
        ),
        migrations.RemoveField(
            model_name='userproject',
            name='user',
        ),
        migrations.RemoveField(
            model_name='topwords',
            name='uploaded_at',
        ),
        migrations.DeleteModel(
            name='UserProject',
        ),
    ]
