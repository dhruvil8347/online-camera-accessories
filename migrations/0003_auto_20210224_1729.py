# Generated by Django 3.1.5 on 2021-02-24 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0002_remove_customer_datejoined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobileNo',
            field=models.BigIntegerField(),
        ),
    ]
