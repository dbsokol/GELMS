# Generated by Django 2.1.3 on 2018-12-01 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='course',
        ),
    ]
