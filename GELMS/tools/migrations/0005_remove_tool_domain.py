# Generated by Django 2.1.3 on 2018-12-01 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0004_auto_20181201_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tool',
            name='domain',
        ),
    ]
