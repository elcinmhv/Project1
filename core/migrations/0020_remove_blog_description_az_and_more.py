# Generated by Django 5.0.2 on 2024-03-23 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_alter_category_options_alter_color_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='description_az',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='description_tr',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_az',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='title_tr',
        ),
    ]
