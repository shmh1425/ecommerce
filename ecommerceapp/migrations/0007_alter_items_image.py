# Generated by Django 4.2.15 on 2024-09-01 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0006_alter_cart_itemsid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
