# Generated by Django 4.0.3 on 2022-07-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0004_alter_program_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='program',
            name='data',
            field=models.CharField(max_length=200, verbose_name='Дата'),
        ),
    ]
