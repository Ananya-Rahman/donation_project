# Generated by Django 3.1 on 2020-09-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_donation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='Description',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='donation',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
