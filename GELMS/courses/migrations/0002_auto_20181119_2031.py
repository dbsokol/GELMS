# Generated by Django 2.1.3 on 2018-11-20 01:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ManyToManyField(limit_choices_to={'custom_user.uid': 1920}, to=settings.AUTH_USER_MODEL),
        ),
    ]
