# Generated by Django 4.0.3 on 2022-07-09 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('en', '0009_remove_program_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='сomitet',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='en.comitettype', verbose_name='Комитет'),
        ),
    ]
