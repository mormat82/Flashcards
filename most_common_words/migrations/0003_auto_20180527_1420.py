# Generated by Django 2.0.2 on 2018-05-27 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('most_common_words', '0002_auto_20180527_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topwords',
            name='user_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='most_common_words.UserProject'),
        ),
        migrations.AlterField(
            model_name='userproject',
            name='name_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload_file.Document'),
        ),
    ]
