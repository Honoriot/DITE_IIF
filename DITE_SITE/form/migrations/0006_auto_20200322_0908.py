# Generated by Django 3.0.4 on 2020-03-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_auto_20200319_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Phone_No',
            field=models.IntegerField(null=True),
        ),
    ]
