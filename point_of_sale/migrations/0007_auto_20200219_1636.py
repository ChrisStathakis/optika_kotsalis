# Generated by Django 2.2.6 on 2020-02-19 14:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0006_auto_20200218_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_expired',
            field=models.DateField(default=datetime.date(2020, 2, 19), verbose_name='Ημερομηνία'),
        ),
    ]
