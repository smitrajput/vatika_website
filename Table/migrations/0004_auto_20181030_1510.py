# Generated by Django 2.1.2 on 2018-10-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Table', '0003_auto_20181030_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktable',
            name='date',
            field=models.DateField(),
        ),
    ]
