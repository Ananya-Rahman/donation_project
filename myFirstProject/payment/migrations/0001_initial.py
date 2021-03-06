# Generated by Django 3.1 on 2020-10-03 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('donate', '0002_auto_20200928_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.TextField(max_length=100)),
                ('transaction_date', models.DateField(blank=True, null=True)),
                ('donate_amount', models.FloatField(blank=True, null=True)),
                ('phone_number', models.FloatField(blank=True, null=True)),
                ('address', models.TextField(max_length=100)),
                ('donate', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='donate.donate')),
            ],
        ),
    ]
