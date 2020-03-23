# Generated by Django 3.0.4 on 2020-03-19 05:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FORM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField()),
                ('Email', models.EmailField(max_length=256)),
                ('Phone_No', models.IntegerField(max_length=11)),
                ('College_Name', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('Suggestions', models.TextField(help_text='Improvement is important..')),
                ('Featured', models.BooleanField()),
            ],
        ),
    ]