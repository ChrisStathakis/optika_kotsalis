# Generated by Django 2.2.6 on 2020-02-21 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0009_auto_20200220_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='eng_title',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Τιτλος για την Αγγλικη Εκδοση'),
        ),
    ]
