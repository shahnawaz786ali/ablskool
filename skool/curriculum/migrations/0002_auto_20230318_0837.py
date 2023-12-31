# Generated by Django 3.2.17 on 2023-03-18 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date_added'], 'verbose_name_plural': '4. Comments'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['position'], 'verbose_name_plural': '3. Lessons'},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name_plural': '5. Replies'},
        ),
        migrations.AlterModelOptions(
            name='standard',
            options={'verbose_name_plural': '1. Standards'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name_plural': '2. Subjects'},
        ),
    ]
