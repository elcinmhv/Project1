# Generated by Django 5.0.2 on 2024-03-02 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_color_alter_category_options_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Kategori', 'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name': 'Renk', 'verbose_name_plural': 'Renkler'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Ürün', 'verbose_name_plural': 'Ürünler'},
        ),
    ]
