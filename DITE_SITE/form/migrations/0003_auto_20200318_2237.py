# Generated by Django 3.0.4 on 2020-03-19 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0002_auto_20200318_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Name',
            field=models.CharField(help_text='User Name', max_length=15),
        ),
    ]
