# Generated by Django 3.2.7 on 2021-11-03 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0019_amocrmpage_amo_implementation_price_third'),
    ]

    operations = [
        migrations.CreateModel(
            name='amoCRMpage_amo_Implementation_price_Fourth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amo_Implementation_priceTitle', models.CharField(max_length=255, verbose_name='Название тарифа внедрения amoCRM')),
                ('amo_Implementation_priceText1', models.TextField(max_length=255, verbose_name='Пункт 1 тарифа')),
                ('amo_Implementation_priceText2', models.TextField(max_length=255, verbose_name='Пункт 2 тарифа')),
                ('amo_Implementation_priceText3', models.TextField(max_length=255, verbose_name='Пункт 3 тарифа')),
                ('amo_Implementation_priceText4', models.TextField(max_length=255, verbose_name='Пункт 4 тарифа')),
                ('amo_Implementation_priceText5', models.TextField(max_length=255, verbose_name='Пункт 5 тарифа')),
            ],
            options={
                'verbose_name': 'amoCRM | Экран с Третьим тарифом amoCRM',
                'verbose_name_plural': 'amoCRM | Экран с Третьим тарифом amoCRM',
            },
        ),
    ]
