# Generated by Django 4.0.3 on 2022-07-09 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('en', '0004_alter_client_country_alter_сomitet_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to='en.participantcategories', verbose_name='Категория участника'),
        ),
    ]
