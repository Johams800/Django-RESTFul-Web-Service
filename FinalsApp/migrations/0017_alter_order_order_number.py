# Generated by Django 3.2 on 2022-05-15 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalsApp', '0016_orderitems_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]