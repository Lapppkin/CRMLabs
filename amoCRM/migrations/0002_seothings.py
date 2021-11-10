# Generated by Django 3.2.7 on 2021-11-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amoCRM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='seoThings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pageTitle', models.CharField(max_length=255, verbose_name='SEO Заголовок страницы')),
                ('pageDescription', models.TextField(max_length=255, verbose_name='SEO Описание страницы')),
            ],
            options={
                'verbose_name': 'SEO | Настройки',
                'verbose_name_plural': 'SEO | Настройки',
            },
        ),
    ]