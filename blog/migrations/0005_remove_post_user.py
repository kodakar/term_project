# Generated by Django 4.1.2 on 2023-01-11 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
    ]