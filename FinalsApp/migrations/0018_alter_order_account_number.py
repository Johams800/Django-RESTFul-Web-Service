# Generated by Django 3.2 on 2022-05-15 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalsApp', '0017_alter_order_order_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='account_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
