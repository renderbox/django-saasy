# Generated by Django 3.0.9 on 2020-08-24 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saasy', '0002_auto_20200824_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=80, verbose_name='Name'),
        ),
    ]
