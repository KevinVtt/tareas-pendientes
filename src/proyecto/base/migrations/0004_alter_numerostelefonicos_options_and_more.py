# Generated by Django 5.0.7 on 2024-07-12 05:03

import django_countries.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_numerostelefonicos_numero_telefono'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='numerostelefonicos',
            options={'ordering': ['numero_telefono']},
        ),
        migrations.AlterField(
            model_name='numerostelefonicos',
            name='nacionalidad',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
