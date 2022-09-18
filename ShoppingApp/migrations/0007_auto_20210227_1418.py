# Generated by Django 3.1.5 on 2021-02-27 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ShoppingApp', '0006_auto_20210226_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='returnPolicy',
            field=models.TextField(default='1 year manufacturer warranty for device and 6 months manufacturer warranty for in-box accessories', max_length=200),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='All Category', on_delete=django.db.models.deletion.CASCADE, to='ShoppingApp.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('black', 'Black'), ('red', 'Red'), ('white', 'White'), ('blue', 'Blue'), ('silver', 'Silver')], default='black', max_length=6),
        ),
        migrations.AlterField(
            model_name='product',
            name='companyName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='ram',
            field=models.CharField(choices=[('None', 'None'), ('2', '2GB'), ('3', '3GB'), ('4', '4GB'), ('6', '6GB'), ('8', '8GB'), ('12', '12GB'), ('16', '16GB'), ('32', '32GB')], default='None', max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='specialOfferDesc',
            field=models.TextField(default='No Special Offer', max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='storage',
            field=models.CharField(choices=[('None', 'None'), ('16', '16GB'), ('32', '32GB'), ('64', '64GB'), ('128', '128GB'), ('256', '256GB'), ('512', '512GB'), ('1024', '1TB')], default='None', max_length=5),
        ),
    ]
