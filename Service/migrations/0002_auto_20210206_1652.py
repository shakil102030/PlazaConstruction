# Generated by Django 3.1.5 on 2021-02-06 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Service', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
    ]
