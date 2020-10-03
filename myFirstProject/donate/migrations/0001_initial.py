# Generated by Django 3.1 on 2020-09-24 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('bkash_number', models.FloatField(blank=True, null=True)),
                ('transaction_id', models.FloatField(blank=True, null=True)),
                ('transaction_date', models.DateField(blank=True, null=True)),
                ('donate_amount', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]