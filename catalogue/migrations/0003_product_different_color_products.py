# Generated by Django 2.2 on 2019-10-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20190920_0732'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='different_color_products',
            field=models.ManyToManyField(blank='True', related_name='_product_different_color_products_+', to='catalogue.Product'),
        ),
    ]
