from django.db import models

# Create your models here.
class Bitrix24page_BannerUp(models.Model):
    bannerUpTitle = models.CharField(max_length=255, verbose_name='Заголовок Главного Баннера')
    bannerUpText = models.TextField(max_length=255, verbose_name='Текст Главного Баннера')


    def __str__(self):
        return self.bannerUpTitle

    class Meta:
        verbose_name = 'Битрикс24 | Первый экран'
        verbose_name_plural = 'Битрикс24 | Первый экран'


class Bitrix24page_Certificate(models.Model):
    certificateImg = models.ImageField(upload_to='bannerimg/', verbose_name='Картинка Сертификата партнера Б24')
    certificateTitle = models.CharField(max_length=255, verbose_name='Название Сертификата партнера Б24')


    def __str__(self):
        return self.certificateTitle

    class Meta:
        verbose_name = 'Битрикс24 | Экран сертификатов'
        verbose_name_plural = 'Битрикс24 | Экран сертификатов'


class b24seoThings(models.Model):
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