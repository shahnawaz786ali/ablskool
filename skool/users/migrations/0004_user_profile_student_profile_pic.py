# Generated by Django 3.2.17 on 2023-05-25 12:16

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_attendance_attendancereport_feedbackstudent_notificationstudent_studentresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile_student',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=users.models.save_profile_image, verbose_name='Profile Image'),
        ),
    ]
