# Generated by Django 3.2 on 2022-05-13 04:38

import FinalsApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalsApp', '0010_remove_order_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='expiration_date',
            field=models.DateField(default=FinalsApp.models.expire),
        ),
    ]