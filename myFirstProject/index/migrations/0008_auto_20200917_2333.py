# Generated by Django 3.1 on 2020-09-17 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20200917_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='image',
            field=models.ImageField(upload_to='donation/'),
        ),
    ]