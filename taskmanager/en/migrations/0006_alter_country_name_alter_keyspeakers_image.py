# Generated by Django 4.0.3 on 2022-07-09 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('en', '0005_alter_participant_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='keyspeakers',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Фото'),
        ),
    ]