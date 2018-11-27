# Generated by Django 2.1.3 on 2018-11-27 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=1000)),
                ('publish_date', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_announcements', to='courses.Course')),
            ],
        ),
    ]
