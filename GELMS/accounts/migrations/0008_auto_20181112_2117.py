# Generated by Django 2.1 on 2018-11-13 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20181112_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='courses',
            field=models.ManyToManyField(to='courses.Course'),
        ),
    ]