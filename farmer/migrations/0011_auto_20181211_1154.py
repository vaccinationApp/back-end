# Generated by Django 2.1.3 on 2018-12-11 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmer', '0010_auto_20181211_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='coordinate',
            field=models.CharField(blank=True, help_text='Координаты дома(можно посмотреть в google map)', max_length=1000, null=True, verbose_name='Координаты'),
        ),
    ]