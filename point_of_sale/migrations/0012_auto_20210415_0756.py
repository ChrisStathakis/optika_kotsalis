# Generated by Django 2.2.4 on 2021-04-15 04:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('point_of_sale', '0011_auto_20200920_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_expired',
            field=models.DateField(default=datetime.date(2021, 4, 15), verbose_name='Ημερομηνία'),
        ),
    ]
