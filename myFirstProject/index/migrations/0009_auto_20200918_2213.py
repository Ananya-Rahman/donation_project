# Generated by Django 3.1 on 2020-09-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0008_auto_20200917_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donation',
            old_name='Description',
            new_name='description',
        ),
        migrations.AddField(
            model_name='donation',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]