# Generated by Django 5.0.2 on 2024-03-25 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_remove_blog_description_az_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='description_tr',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_tr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]