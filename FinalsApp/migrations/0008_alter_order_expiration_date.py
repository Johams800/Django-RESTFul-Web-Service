# Generated by Django 3.2 on 2022-05-13 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalsApp', '0007_order_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='expiration_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 13, 0, 32, 23, 841119)),
        ),
    ]
