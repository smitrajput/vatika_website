# Generated by Django 2.1.2 on 2018-11-11 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20181111_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='item_price',
            field=models.CharField(max_length=6),
        ),
    ]
