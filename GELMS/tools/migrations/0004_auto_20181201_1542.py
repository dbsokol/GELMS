# Generated by Django 2.1.3 on 2018-12-01 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0003_tool_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='domain',
            field=models.CharField(max_length=30),
        ),
    ]
