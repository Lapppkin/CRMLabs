from django.db import models

# Create your models here.
class Header_phone(models.Model):
    phone = models.CharField(max_length=200, verbose_name='Телефон')


    def __str__(self):
        return self.phone

    class Meta:
        verbose_name = 'Номер телефона'
        verbose_name_plural = 'Номера телефонов'


class Footer_email(models.Model):
    email_text = models.CharField(max_length=200, verbose_name='Email')


    def __str__(self):
        return self.email_text


    class Meta:
        verbose_name = 'Email'


class Footer_address_krd(models.Model):
    address_krd = models.CharField(max_length=200, verbose_name='Краснодарский адрес')


    def __str__(self):
        return self.address_krd


    class Meta:
        verbose_name = 'Краснодарский адрес'
        verbose_name_plural = 'Краснодарские адреса'


class Footer_address_msk(models.Model):
    address_msk = models.CharField(max_length=200, verbose_name='Московский адрес')


    def __str__(self):
        return self.address_msk

    class Meta:
        verbose_name = 'Московский адрес'
        verbose_name_plural = 'Московские адреса'