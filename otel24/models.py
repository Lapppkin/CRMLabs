from django.db import models

# Create your models here.
class otel24page_BannerUp(models.Model):
    bannerTitle = models.CharField(max_length=255, verbose_name='Заголовок Главного Экрана')


    def __str__(self):
        return self.bannerTitle

    class Meta:
        verbose_name = 'Отель24 | Первый экран'
        verbose_name_plural = 'Отель24 | Первый экран'


class otel24seoThings(models.Model):
    pageTitle = models.CharField(max_length=210, 
                                blank=True, 
                                help_text='длина до 210 символов, заполнять обязательно', 
                                verbose_name='SEO Заголовок страницы')
    pageDescription = models.TextField(max_length=450,
                                        blank=True, 
                                        help_text='длина до 450 символов, заполнять обязательно', 
                                        verbose_name='SEO Описание страницы')


    def __str__(self):
        return self.pageTitle

    class Meta:
        verbose_name = 'SEO | Настройки'
        verbose_name_plural = 'SEO | Настройки'


class setupRateOne(models.Model):
    setupRateTitle = models.CharField(max_length=255, verbose_name='Название тарифа внедрения Отель24')
    setupRateText1 = models.TextField(max_length=555, verbose_name='Пункт 1 тарифа')
    setupRateText2 = models.TextField(max_length=555, verbose_name='Пункт 2 тарифа')
    setupRateText3 = models.TextField(max_length=555, verbose_name='Пункт 3 тарифа')
    setupRateText4 = models.TextField(max_length=555, verbose_name='Пункт 4 тарифа')
    setupRatePrice = models.CharField(max_length=255, verbose_name='Стоимость тарифа Отель24')
    setupRateDays = models.CharField(max_length=255, verbose_name='Срок выполнения работ')


    def __str__(self):
        return self.setupRateTitle

    class Meta:
        verbose_name = 'Стоимость первого тарифа Отель24'
        verbose_name_plural = 'Стоимость первого тарифа Отель24'


class setupRateTwo(models.Model):
    setupRateTitle = models.CharField(max_length=255, verbose_name='Название тарифа внедрения Отель24')
    setupRateText1 = models.TextField(max_length=555, verbose_name='Пункт 1 тарифа')
    setupRateText2 = models.TextField(max_length=555, verbose_name='Пункт 2 тарифа')
    setupRateText3 = models.TextField(max_length=555, verbose_name='Пункт 3 тарифа')
    setupRateText4 = models.TextField(max_length=555, verbose_name='Пункт 4 тарифа')
    setupRateText5 = models.TextField(max_length=555, verbose_name='Пункт 5 тарифа')
    setupRateText6 = models.TextField(max_length=555, verbose_name='Пункт 6 тарифа')
    setupRatePrice = models.CharField(max_length=255, verbose_name='Стоимость тарифа Отель24')
    setupRateDays = models.CharField(max_length=255, verbose_name='Срок выполнения работ')


    def __str__(self):
        return self.setupRateTitle

    class Meta:
        verbose_name = 'Стоимость второго тарифа Отель24'
        verbose_name_plural = 'Стоимость второго тарифа Отель24'


class setupRateThree(models.Model):
    setupRateTitle = models.CharField(max_length=255, verbose_name='Название тарифа внедрения Отель24')
    setupRateText1 = models.TextField(max_length=555, verbose_name='Пункт 1 тарифа')
    setupRateText2 = models.TextField(max_length=555, verbose_name='Пункт 2 тарифа')
    setupRateText3 = models.TextField(max_length=555, verbose_name='Пункт 3 тарифа')
    setupRateText4 = models.TextField(max_length=555, verbose_name='Пункт 4 тарифа')
    setupRatePrice = models.CharField(max_length=255, verbose_name='Стоимость тарифа Отель24')
    setupRateDays = models.CharField(max_length=255, verbose_name='Срок выполнения работ')


    def __str__(self):
        return self.setupRateTitle

    class Meta:
        verbose_name = 'Стоимость третьего тарифа Отель24'
        verbose_name_plural = 'Стоимость третьего тарифа Отель24'