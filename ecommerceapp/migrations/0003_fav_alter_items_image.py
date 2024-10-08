# Generated by Django 4.2.15 on 2024-08-31 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='fav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemid', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='items',
            name='image',
            field=models.ImageField(null=True, upload_to='\\images'),
        ),
    ]
