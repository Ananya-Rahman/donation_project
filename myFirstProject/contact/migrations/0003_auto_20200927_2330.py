# Generated by Django 3.1 on 2020-09-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200927_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.TextField(max_length=200),
        ),
    ]
