# Generated by Django 2.1.3 on 2018-11-20 01:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('domain', models.CharField(max_length=200)),
                ('people', models.ManyToManyField(blank=True, related_name='people', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ManyToManyField(limit_choices_to={'id': 1}, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
