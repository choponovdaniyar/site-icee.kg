# Generated by Django 4.0.3 on 2022-07-09 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0005_program_date_alter_program_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='data',
        ),
    ]
