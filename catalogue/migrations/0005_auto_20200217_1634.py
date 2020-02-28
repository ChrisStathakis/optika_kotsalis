# Generated by Django 2.2.6 on 2020-02-17 14:34

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20191104_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='eng_title',
            field=models.CharField(max_length=250, null=True, verbose_name='Τιτλος για την Αγγλικη Εκδοση'),
        ),
        migrations.AddField(
            model_name='category',
            name='eng_title',
            field=models.CharField(max_length=120, null=True, verbose_name='Τιτλος στα Αγγλικα'),
        ),
        migrations.AddField(
            model_name='product',
            name='eng_site_text',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Κειμενο για την Αγγλικη Εκδοση'),
        ),
        migrations.AddField(
            model_name='product',
            name='eng_title',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Τιτλος για την Αγγλικη Εκδοση'),
        ),
        migrations.AlterField(
            model_name='characteristics',
            name='ordering_by_letter',
            field=models.CharField(default='c', max_length=15, verbose_name='Ταξινομηση με γραμμα'),
        ),
        migrations.AlterField(
            model_name='characteristicsvalue',
            name='ordering_by_letter',
            field=models.CharField(default='c', max_length=15, verbose_name='Ταξινομηση με γραμμα'),
        ),
        migrations.AlterField(
            model_name='color',
            name='title',
            field=models.CharField(max_length=250, verbose_name='Τιτλος για την Αγγλικη Εκδοση'),
        ),
        migrations.AlterField(
            model_name='product',
            name='ordering_by_letter',
            field=models.CharField(default='c', max_length=15, verbose_name='Ταξινομηση με γραμμα'),
        ),
    ]