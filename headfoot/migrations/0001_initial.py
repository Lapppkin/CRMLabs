# Generated by Django 3.2.7 on 2021-10-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footer_address_krd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_krd', models.CharField(max_length=200, verbose_name='Краснодарский адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Footer_address_msk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_msk', models.CharField(max_length=200, verbose_name='Московский адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Footer_email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_text', models.CharField(max_length=200, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Header_phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.IntegerField(verbose_name='Телефон')),
            ],
        ),
    ]