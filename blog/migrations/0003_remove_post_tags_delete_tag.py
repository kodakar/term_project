# Generated by Django 4.1.2 on 2023-01-08 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag_remove_post_category_delete_category_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
