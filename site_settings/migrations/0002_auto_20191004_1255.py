# Generated by Django 2.2 on 2019-10-04 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='category',
            field=models.CharField(choices=[('a', 'Μεγάλο Banner --> (1970*718)'), ('b', 'Μεσαίο Banner --> No Use. For future'), ('c', 'Μικρό Banner -->(1000*550)')], default='a', max_length=1),
        ),
    ]