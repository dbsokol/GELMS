# Generated by Django 2.1 on 2018-11-17 15:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_course_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='people',
            field=models.ManyToManyField(blank=True, related_name='people', to=settings.AUTH_USER_MODEL),
        ),
    ]