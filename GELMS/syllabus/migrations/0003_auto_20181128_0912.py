# Generated by Django 2.1.3 on 2018-11-28 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0002_auto_20181128_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]