# Generated by Django 3.2 on 2022-05-13 04:05

import FinalsApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalsApp', '0006_remove_order_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expiration_date',
            field=models.DateTimeField(default=FinalsApp.models.expire),
        ),
    ]
