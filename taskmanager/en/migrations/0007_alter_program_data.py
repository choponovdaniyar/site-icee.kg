# Generated by Django 4.0.3 on 2022-07-09 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('en', '0006_alter_country_name_alter_keyspeakers_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='data',
            field=models.DateField(verbose_name='Дата'),
        ),
    ]
