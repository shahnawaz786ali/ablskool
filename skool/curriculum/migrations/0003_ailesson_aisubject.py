# Generated by Django 3.2.17 on 2023-03-28 11:59

import curriculum.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('curriculum', '0002_auto_20230318_0837'),
    ]

    operations = [
        migrations.CreateModel(
            name='AISubject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=curriculum.models.save_subject_image, verbose_name='Coding Subject Image')),
                ('description', models.TextField(blank=True, max_length=500)),
            ],
            options={
                'verbose_name_plural': 'AISubjects',
            },
        ),
        migrations.CreateModel(
            name='AILesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_id', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('position', models.PositiveSmallIntegerField(verbose_name='Chapter no.')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('video', models.FileField(blank=True, null=True, upload_to=curriculum.models.save_lesson_files, verbose_name='CodingVideo')),
                ('created_by', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coding_lessons', to='curriculum.aisubject')),
            ],
            options={
                'verbose_name_plural': 'AILessons',
                'ordering': ['position'],
            },
        ),
    ]
