# Generated by Django 5.0.2 on 2024-02-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_category_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='surname',
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]