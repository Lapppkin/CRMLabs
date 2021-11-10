# Generated by Django 3.2.7 on 2021-11-08 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitrix24', '0002_remove_bitrix24page_bannerup_bannerupimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bitrix24page_Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificateImg', models.ImageField(upload_to='bannerimg/', verbose_name='Картинка Сертификата партнера Б24')),
            ],
            options={
                'verbose_name': 'Битрикс24 | Экран сертификатов',
                'verbose_name_plural': 'Битрикс24 | Экран сертификатов',
            },
        ),
    ]
