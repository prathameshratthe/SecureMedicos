# Generated by Django 3.0.3 on 2020-03-05 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20200221_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='key',
        ),
    ]