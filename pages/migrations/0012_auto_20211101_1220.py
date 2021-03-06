# Generated by Django 3.2.7 on 2021-11-01 09:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_amocrmpage_amo_price_amo_priceprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amocrmpage_amo_price',
            name='amo_priceText',
        ),
        migrations.AddField(
            model_name='amocrmpage_amo_price',
            name='amo_priceText1',
            field=models.TextField(default=django.utils.timezone.now, max_length=255, verbose_name='Пункт 1 тарифа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amocrmpage_amo_price',
            name='amo_priceText2',
            field=models.TextField(default=django.utils.timezone.now, max_length=255, verbose_name='Пункт 2 тарифа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amocrmpage_amo_price',
            name='amo_priceText3',
            field=models.TextField(default=django.utils.timezone.now, max_length=255, verbose_name='Пункт 3 тарифа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amocrmpage_amo_price',
            name='amo_priceText4',
            field=models.TextField(default=django.utils.timezone.now, max_length=255, verbose_name='Пункт 4 тарифа'),
            preserve_default=False,
        ),
    ]
