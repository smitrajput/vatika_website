# Generated by Django 2.1.2 on 2018-11-04 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Table', '0004_auto_20181030_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktable',
            name='contact',
            field=models.CharField(max_length=10),
        ),
    ]
