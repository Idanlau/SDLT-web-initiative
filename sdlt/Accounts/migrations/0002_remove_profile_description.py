# Generated by Django 3.0.5 on 2020-04-09 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
    ]