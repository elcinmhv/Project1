# Generated by Django 5.0.2 on 2024-02-16 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='surname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
