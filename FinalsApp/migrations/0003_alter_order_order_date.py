# Generated by Django 3.2 on 2022-05-13 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalsApp', '0002_alter_orderitems_item_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now=True),
        ),
    ]
