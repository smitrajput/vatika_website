# Generated by Django 2.1.2 on 2018-11-11 23:46

from django.db import migrations, models
import home.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact',
            field=models.CharField(max_length=10, validators=[home.models.validate_contact]),
        ),
    ]