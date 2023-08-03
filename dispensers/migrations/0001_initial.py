# Generated by Django 4.2.4 on 2023-08-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispenser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flow_volume', models.DecimalField(decimal_places=2, max_digits=5)),
                ('is_open', models.BooleanField(default=False)),
                ('opened_at', models.DateTimeField(blank=True, null=True)),
                ('closed_at', models.DateTimeField(blank=True, null=True)),
                ('total_money', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
    ]
