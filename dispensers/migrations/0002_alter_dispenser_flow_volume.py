# Generated by Django 4.2.4 on 2023-08-03 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispensers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dispenser',
            name='flow_volume',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
