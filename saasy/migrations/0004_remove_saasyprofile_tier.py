# Generated by Django 3.1.1 on 2021-01-30 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saasy', '0003_auto_20200824_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saasyprofile',
            name='tier',
        ),
    ]
