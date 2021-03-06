# Generated by Django 3.2.7 on 2021-11-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_auto_20211102_1336'),
    ]

    operations = [
        migrations.CreateModel(
            name='amoCRMpage_amo_Implementation_price_Second',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amo_Implementation_priceTitle', models.CharField(max_length=255, verbose_name='Название тарифа внедрения amoCRM')),
                ('amo_Implementation_priceText1', models.TextField(max_length=255, verbose_name='Пункт 1 тарифа')),
                ('amo_Implementation_priceText2', models.TextField(max_length=255, verbose_name='Пункт 2 тарифа')),
                ('amo_Implementation_priceText3', models.TextField(max_length=255, verbose_name='Пункт 3 тарифа')),
                ('amo_Implementation_priceText4', models.TextField(max_length=255, verbose_name='Пункт 4 тарифа')),
                ('amo_Implementation_priceText5', models.TextField(max_length=255, verbose_name='Пункт 5 тарифа')),
                ('amo_Implementation_priceText6', models.TextField(max_length=255, verbose_name='Пункт 6 тарифа')),
                ('amo_Implementation_priceText7', models.TextField(max_length=255, verbose_name='Пункт 7 тарифа')),
                ('amo_Implementation_priceText8', models.TextField(max_length=255, verbose_name='Пункт 8 тарифа')),
                ('amo_Implementation_priceText9', models.TextField(max_length=255, verbose_name='Пункт 9 тарифа')),
                ('amo_Implementation_priceText10', models.TextField(max_length=255, verbose_name='Пункт 10 тарифа')),
                ('amo_Implementation_priceText11', models.TextField(max_length=255, verbose_name='Пункт 11 тарифа')),
                ('amo_Implementation_priceText12', models.TextField(max_length=255, verbose_name='Пункт 12 тарифа')),
                ('amo_Implementation_priceText13', models.TextField(max_length=255, verbose_name='Пункт 13 тарифа')),
                ('amo_Implementation_priceText14', models.TextField(max_length=255, verbose_name='Пункт 14 тарифа')),
                ('amo_Implementation_priceText15', models.TextField(max_length=555, verbose_name='Пункт 15 тарифа')),
                ('amo_Implementation_priceText16', models.TextField(max_length=255, verbose_name='Пункт 16 тарифа')),
                ('amo_Implementation_priceText17', models.TextField(max_length=555, verbose_name='Пункт 17 тарифа')),
                ('amo_Implementation_priceText18', models.TextField(max_length=555, verbose_name='Пункт 18 тарифа')),
                ('amo_Implementation_priceText19', models.TextField(max_length=555, verbose_name='Пункт 19 тарифа')),
                ('amo_Implementation_priceText20', models.TextField(max_length=555, verbose_name='Пункт 20 тарифа')),
                ('amo_Implementation_priceText21', models.TextField(max_length=555, verbose_name='Пункт 21 тарифа')),
                ('amo_Implementation_priceText22', models.TextField(max_length=555, verbose_name='Пункт 22 тарифа')),
                ('amo_Implementation_priceText23', models.TextField(max_length=555, verbose_name='Пункт 23 тарифа')),
                ('amo_Implementation_priceText24', models.TextField(max_length=555, verbose_name='Пункт 24 тарифа')),
                ('amo_Implementation_priceText25', models.TextField(max_length=555, verbose_name='Пункт 25 тарифа')),
                ('amo_Implementation_priceText26', models.TextField(max_length=555, verbose_name='Пункт 26 тарифа')),
                ('amo_Implementation_pricePrice', models.CharField(max_length=255, verbose_name='Стоимость тарифа amoCRM')),
                ('amo_Implementation_priceDays', models.CharField(max_length=255, verbose_name='Срок выполнения работ')),
            ],
            options={
                'verbose_name': 'amoCRM | Экран со Вторым тарифом amoCRM',
                'verbose_name_plural': 'amoCRM | Экран со Вторым тарифом amoCRM',
            },
        ),
    ]
