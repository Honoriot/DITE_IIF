# Generated by Django 3.0.4 on 2020-03-19 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20200318_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Phone_No',
            field=models.IntegerField(),
        ),
    ]
