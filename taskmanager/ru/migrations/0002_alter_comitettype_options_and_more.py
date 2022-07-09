# Generated by Django 4.0.3 on 2022-07-09 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comitettype',
            options={'verbose_name': 'Комитет', 'verbose_name_plural': 'Комитеты'},
        ),
        migrations.AlterModelOptions(
            name='participantcategories',
            options={'verbose_name': 'Категория участника конференции', 'verbose_name_plural': 'Категории участников конференции'},
        ),
        migrations.AlterModelOptions(
            name='сomitet',
            options={'ordering': ('name',), 'verbose_name': 'Член комитет', 'verbose_name_plural': 'Члены Комитета'},
        ),
    ]
