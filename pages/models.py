# from django.db import models

# # Create your models here.
# class amoCRMpage_BannerUp(models.Model):
#     bannerUpImg = models.ImageField(upload_to='bannerimg/', verbose_name='Картинка Главного Баннера')
#     bannerUpTitle = models.CharField(max_length=255, verbose_name='Заголовок Главного Баннера')
#     bannerUpText = models.TextField(max_length=255, verbose_name='Текст Главного Баннера')


#     def __str__(self):
#         return self.bannerUpTitle

#     class Meta:
#         verbose_name = 'amoCRM | Первый экран'
#         verbose_name_plural = 'amoCRM | Первый экран'


# class amoCRMpage_BasicTerms(models.Model):
#     basicTermsTitle = models.CharField(max_length=255, verbose_name='Заголовок слева')
#     basicTermsMiniTitle = models.CharField(max_length=255, verbose_name='Маленький Заголовок справа')
#     basicTermsText1 = models.TextField(max_length=255, verbose_name='Пункт 1 под правым заголовком')
#     basicTermsText2 = models.TextField(max_length=255, verbose_name='Пункт 2 под правым заголовком')
#     basicTermsText3 = models.TextField(max_length=255, verbose_name='Пункт 3 под правым заголовком')



#     def __str__(self):
#         return self.basicTermsTitle

#     class Meta:
#         verbose_name = 'amoCRM | Второй экран'
#         verbose_name_plural = 'amoCRM | Второй экран'


# class amoCRMpage_CrmTypes(models.Model):
#     crmTypesTitle = models.CharField(max_length=255, verbose_name='Заголовок в центре')
#     crmTypesLeftMiniTitle = models.CharField(max_length=255, verbose_name='Маленький Заголовок слева')
#     crmTypesLeftText1 = models.TextField(max_length=255, verbose_name='Пункт 1 под левым заголовком')
#     crmTypesLeftText2 = models.TextField(max_length=255, verbose_name='Пункт 2 под левым заголовком')
#     crmTypesLeftText3 = models.TextField(max_length=255, verbose_name='Пункт 3 под левым заголовком')
#     crmTypesRightMiniTitle = models.CharField(max_length=255, verbose_name='Маленький Заголовок справа')
#     crmTypesRightText1 = models.TextField(max_length=255, verbose_name='Пункт 1 под правым заголовком')
#     crmTypesRightText2 = models.TextField(max_length=255, verbose_name='Пункт 2 под правым заголовком')



#     def __str__(self):
#         return self.crmTypesTitle

#     class Meta:
#         verbose_name = 'amoCRM | Третий экран'
#         verbose_name_plural = 'amoCRM | Третий экран'


# class amoCRMpage_CrmAdvantages(models.Model):
#     crmAdvantagesImg = models.ImageField(upload_to='amopageimg/', verbose_name='Картинка слева от текста')
#     crmAdvantagesTitle = models.CharField(max_length=255, verbose_name='Заголовок в центре')
#     crmAdvantagesTitle1 = models.CharField(max_length=255, verbose_name='Заголовок справа 1')
#     crmAdvantagesText1 = models.TextField(max_length=255, verbose_name='Пункт 1 под правым заголовком')
#     crmAdvantagesText2 = models.TextField(max_length=255, verbose_name='Пункт 2 под правым заголовком')
#     crmAdvantagesText3 = models.TextField(max_length=255, verbose_name='Пункт 3 под правым заголовком')
#     crmAdvantagesText4 = models.TextField(max_length=255, verbose_name='Пункт 4 под правым заголовком')
#     crmAdvantagesText5 = models.TextField(max_length=255, verbose_name='Пункт 5 под правым заголовком')
#     crmAdvantagesText6 = models.TextField(max_length=255, verbose_name='Пункт 6 под правым заголовком')
#     crmAdvantagesText7 = models.TextField(max_length=255, verbose_name='Пункт 7 под правым заголовком')
#     crmAdvantagesTitle2 = models.CharField(max_length=255, verbose_name='Заголовок справа 2')
#     crmAdvantagesTitle3 = models.CharField(max_length=255, verbose_name='Заголовок справа 3')
#     crmAdvantagesTitleLeft = models.CharField(max_length=255, verbose_name='Заголовок слева')
#     crmAdvantagesTextLeft = models.TextField(max_length=255, verbose_name='Текст под левым заголовком')
#     crmAdvantagesImg2 = models.ImageField(upload_to='amopageimg/', verbose_name='Картинка справа от текста')
#     crmAdvantagesStage1 = models.CharField(max_length=255, verbose_name='Этап 1')
#     crmAdvantagesStage2 = models.CharField(max_length=255, verbose_name='Этап 2')
#     crmAdvantagesStage3 = models.CharField(max_length=255, verbose_name='Этап 3')
#     crmAdvantagesStage4 = models.CharField(max_length=255, verbose_name='Этап 4')
#     crmAdvantagesStage5 = models.CharField(max_length=255, verbose_name='Этап 5')
#     crmAdvantagesStage6 = models.CharField(max_length=255, verbose_name='Этап 6')



#     def __str__(self):
#         return self.crmAdvantagesTitle

#     class Meta:
#         verbose_name = 'amoCRM | Четвертый экран'
#         verbose_name_plural = 'amoCRM | Четвертый экран'


# class amoCRMpage_amo_price(models.Model):
#     amo_priceTitle = models.CharField(max_length=255, verbose_name='Название тарифа amoCRM')
#     amo_priceDescription = models.CharField(max_length=255, verbose_name='Описание тарифа')
#     amo_priceText1 = models.TextField(max_length=255, verbose_name='Пункт 1 тарифа')
#     amo_priceText2 = models.TextField(max_length=255, verbose_name='Пункт 2 тарифа')
#     amo_priceText3 = models.TextField(max_length=255, verbose_name='Пункт 3 тарифа')
#     amo_priceText4 = models.TextField(max_length=255, verbose_name='Пункт 4 тарифа')
#     amo_pricePrice = models.CharField(max_length=255, verbose_name='Стоимость тарифа amoCRM')


#     def __str__(self):
#         return self.amo_priceTitle

#     class Meta:
#         verbose_name = 'amoCRM | Экран с тарифами amoCRM'
#         verbose_name_plural = 'amoCRM | Экран с тарифами amoCRM'


# class amoCRMpage_amo_combo_price(models.Model):
#     amo_combo_priceTitle = models.CharField(max_length=255, verbose_name='Название пакетного тарифа amoCRM')
#     amo_combo_priceDescription = models.CharField(max_length=255, verbose_name='Описание пакетного тарифа')
#     amo_combo_priceText1 = models.TextField(max_length=255, verbose_name='Пункт 1 тарифа')
#     amo_combo_priceText2 = models.TextField(max_length=255, verbose_name='Пункт 2 тарифа')
#     amo_combo_pricePrice = models.CharField(max_length=255, verbose_name='Стоимость пакетного тарифа amoCRM')


#     def __str__(self):
#         return self.amo_combo_priceTitle

#     class Meta:
#         verbose_name = 'amoCRM | Экран с пакетными тарифами amoCRM'
#         verbose_name_plural = 'amoCRM | Экран с пакетными тарифами amoCRM'


# class amoCRMpage_amo_Implementation_price_First(models.Model):
#     amo_Implementation_priceTitle = models.CharField(max_length=255, verbose_name='Название тарифа внедрения amoCRM')
#     amo_Implementation_priceText1 = models.TextField(max_length=255, verbose_name='Пункт 1 тарифа')
#     amo_Implementation_priceText2 = models.TextField(max_length=255, verbose_name='Пункт 2 тарифа')
#     amo_Implementation_priceText3 = models.TextField(max_length=255, verbose_name='Пункт 3 тарифа')
#     amo_Implementation_priceText4 = models.TextField(max_length=255, verbose_name='Пункт 4 тарифа')
#     amo_Implementation_priceText5 = models.TextField(max_length=255, verbose_name='Пункт 5 тарифа')
#     amo_Implementation_priceText6 = models.TextField(max_length=255, verbose_name='Пункт 6 тарифа')
#     amo_Implementation_priceText7 = models.TextField(max_length=255, verbose_name='Пункт 7 тарифа')
#     amo_Implementation_priceText8 = models.TextField(max_length=255, verbose_name='Пункт 8 тарифа')
#     amo_Implementation_priceText9 = models.TextField(max_length=255, verbose_name='Пункт 9 тарифа')
#     amo_Implementation_priceText10 = models.TextField(max_length=255, verbose_name='Пункт 10 тарифа')
#     amo_Implementation_priceText11 = models.TextField(max_length=255, verbose_name='Пункт 11 тарифа')
#     amo_Implementation_priceText12 = models.TextField(max_length=255, verbose_name='Пункт 12 тарифа')
#     amo_Implementation_priceText13 = models.TextField(max_length=255, verbose_name='Пункт 13 тарифа')
#     amo_Implementation_priceText14 = models.TextField(max_length=255, verbose_name='Пункт 14 тарифа')
#     amo_Implementation_priceText15 = models.TextField(max_length=555, verbose_name='Пункт 15 тарифа')
#     amo_Implementation_priceText16 = models.TextField(max_length=255, verbose_name='Пункт 16 тарифа')
#     amo_Implementation_priceText17 = models.TextField(max_length=555, verbose_name='Пункт 17 тарифа')
#     amo_Implementation_pricePrice = models.CharField(max_length=255, verbose_name='Стоимость тарифа amoCRM')
#     amo_Implementation_priceDays = models.CharField(max_length=255, verbose_name='Срок выполнения работ')


#     def __str__(self):
#         return self.amo_Implementation_priceTitle

#     class Meta:
#         verbose_name = 'amoCRM | Экран с Первым тарифом amoCRM'
#         verbose_name_plural = 'amoCRM | Экран с Первым тарифом amoCRM'


# class amoCRMpage_amo_Implementation_price_Second(models.Model):
#     amo_Implementation_priceTitle = models.CharField(max_length=255, verbose_name='Название тарифа внедрения amoCRM')
#     amo_Implementation_priceText1 = models.TextField(max_length=255, verbose_name='Пункт 1 тарифа')
#     amo_Implementation_priceText2 = models.TextField(max_length=255, verbose_name='Пункт 2 тарифа')
#     amo_Implementation_priceText3 = models.TextField(max_length=255, verbose_name='Пункт 3 тарифа')
#     amo_Implementation_priceText4 = models.TextField(max_length=255, verbose_name='Пункт 4 тарифа')
#     amo_Implementation_priceText5 = models.TextField(max_length=255, verbose_name='Пункт 5 тарифа')
#     amo_Implementation_priceText6 = models.TextField(max_length=255, verbose_name='Пункт 6 тарифа')
#     amo_Implementation_priceText7 = models.TextField(max_length=255, verbose_name='Пункт 7 тарифа')
#     amo_Implementation_priceText8 = models.TextField(max_length=255, verbose_name='Пункт 8 тарифа')
#     amo_Implementation_priceText9 = models.TextField(max_length=255, verbose_name='Пункт 9 тарифа')
#     amo_Implementation_priceText10 = models.TextField(max_length=255, verbose_name='Пункт 10 тарифа')
#     amo_Implementation_priceText11 = models.TextField(max_length=255, verbose_name='Пункт 11 тарифа')
#     amo_Implementation_priceText12 = models.TextField(max_length=255, verbose_name='Пункт 12 тарифа')
#     amo_Implementation_priceText13 = models.TextField(max_length=255, verbose_name='Пункт 13 тарифа')
#     amo_Implementation_priceText14 = models.TextField(max_length=255, verbose_name='Пункт 14 тарифа')
#     amo_Implementation_priceText15 = models.TextField(max_length=555, verbose_name='Пункт 15 тарифа')
#     amo_Implementation_priceText16 = models.TextField(max_length=255, verbose_name='Пункт 16 тарифа')
#     amo_Implementation_priceText17 = models.TextField(max_length=555, verbose_name='Пункт 17 тарифа')
#     amo_Implementation_priceText18 = models.TextField(max_length=555, verbose_name='Пункт 18 тарифа')
#     amo_Implementation_priceText19 = models.TextField(max_length=555, verbose_name='Пункт 19 тарифа')
#     amo_Implementation_priceText20 = models.TextField(max_length=555, verbose_name='Пункт 20 тарифа')
#     amo_Implementation_priceText21 = models.TextField(max_length=555, verbose_name='Пункт 21 тарифа')
#     amo_Implementation_priceText22 = models.TextField(max_length=555, verbose_name='Пункт 22 тарифа')
#     amo_Implementation_priceText23 = models.TextField(max_length=555, verbose_name='Пункт 23 тарифа')
#     amo_Implementation_priceText24 = models.TextField(max_length=555, verbose_name='Пункт 24 тарифа')
#     amo_Implementation_priceText25 = models.TextField(max_length=555, verbose_name='Пункт 25 тарифа')
#     amo_Implementation_priceText26 = models.TextField(max_length=555, verbose_name='Пункт 26 тарифа')
#     amo_Implementation_pricePrice = models.CharField(max_length=255, verbose_name='Стоимость тарифа amoCRM')
#     amo_Implementation_priceDays = models.CharField(max_length=255, verbose_name='Срок выполнения работ')


#     def __str__(self):
#         return self.amo_Implementation_priceTitle

#     class Meta:
#         verbose_name = 'amoCRM | Экран со Вторым тарифом amoCRM'
#         verbose_name_plural = 'amoCRM | Экран со Вторым тарифом amoCRM'


# class amoCRMpage_amo_Implementation_price_Third(models.Model):
#     amo_Implementation_priceTitle = models.CharField(max_length=255, verbose_name='Название тарифа внедрения amoCRM')
#     amo_Implementation_priceText1 = models.TextField(max_length=255, verbose_name='Пункт 1 тарифа')
#     amo_Implementation_priceText2 = models.TextField(max_length=255, verbose_name='Пункт 2 тарифа')
#     amo_Implementation_priceText3 = models.TextField(max_length=255, verbose_name='Пункт 3 тарифа')
#     amo_Implementation_priceText4 = models.TextField(max_length=255, verbose_name='Пункт 4 тарифа')
#     amo_Implementation_priceText5 = models.TextField(max_length=255, verbose_name='Пункт 5 тарифа')
#     amo_Implementation_priceText6 = models.TextField(max_length=255, verbose_name='Пункт 6 тарифа')
#     amo_Implementation_priceText7 = models.TextField(max_length=255, verbose_name='Пункт 7 тарифа')
#     amo_Implementation_priceText8 = models.TextField(max_length=255, verbose_name='Пункт 8 тарифа')
#     amo_Implementation_priceText9 = models.TextField(max_length=255, verbose_name='Пункт 9 тарифа')
#     amo_Implementation_priceText10 = models.TextField(max_length=255, verbose_name='Пункт 10 тарифа')
#     amo_Implementation_priceText11 = models.TextField(max_length=255, verbose_name='Пункт 11 тарифа')
#     amo_Implementation_priceText12 = models.TextField(max_length=255, verbose_name='Пункт 12 тарифа')
#     amo_Implementation_priceText13 = models.TextField(max_length=255, verbose_name='Пункт 13 тарифа')
#     amo_Implementation_priceText14 = models.TextField(max_length=255, verbose_name='Пункт 14 тарифа')
#     amo_Implementation_priceText15 = models.TextField(max_length=555, verbose_name='Пункт 15 тарифа')
#     amo_Implementation_priceText16 = models.TextField(max_length=255, verbose_name='Пункт 16 тарифа')
#     amo_Implementation_priceText17 = models.TextField(max_length=555, verbose_name='Пункт 17 тарифа')
#     amo_Implementation_priceText18 = models.TextField(max_length=555, verbose_name='Пункт 18 тарифа')
#     amo_Implementation_priceText19 = models.TextField(max_length=555, verbose_name='Пункт 19 тарифа')
#     amo_Implementation_priceText20 = models.TextField(max_length=555, verbose_name='Пункт 20 тарифа')
#     amo_Implementation_priceText21 = models.TextField(max_length=555, verbose_name='Пункт 21 тарифа')
#     amo_Implementation_priceText22 = models.TextField(max_length=555, verbose_name='Пункт 22 тарифа')
#     amo_Implementation_priceText23 = models.TextField(max_length=555, verbose_name='Пункт 23 тарифа')
#     amo_Implementation_priceText24 = models.TextField(max_length=555, verbose_name='Пункт 24 тарифа')
#     amo_Implementation_priceText25 = models.TextField(max_length=555, verbose_name='Пункт 25 тарифа')
#     amo_Implementation_priceText26 = models.TextField(max_length=555, verbose_name='Пункт 26 тарифа')
#     amo_Implementation_priceText27 = models.TextField(max_length=555, verbose_name='Пункт 27 тарифа')
#     amo_Implementation_priceText28 = models.TextField(max_length=555, verbose_name='Пункт 28 тарифа')
#     amo_Implementation_priceText29 = models.TextField(max_length=555, verbose_name='Пункт 29 тарифа')
#     amo_Implementation_priceText30 = models.TextField(max_length=555, verbose_name='Пункт 30 тарифа')
#     amo_Implementation_pricePrice = models.CharField(max_length=255, verbose_name='Стоимость тарифа amoCRM')
#     amo_Implementation_priceDays = models.CharField(max_length=255, verbose_name='Срок выполнения работ')


#     def __str__(self):
#         return self.amo_Implementation_priceTitle

#     class Meta:
#         verbose_name = 'amoCRM | Экран с Третьим тарифом amoCRM'
#         verbose_name_plural = 'amoCRM | Экран с Третьим тарифом amoCRM'


# class amoCRMpage_amo_Implementation_price_Fourth(models.Model):
#     amo_Implementation_priceTitle = models.CharField(max_length=255, verbose_name='Название тарифа внедрения amoCRM')
#     amo_Implementation_priceText1 = models.TextField(max_length=255, verbose_name='Пункт 1 тарифа')
#     amo_Implementation_priceText2 = models.TextField(max_length=255, verbose_name='Пункт 2 тарифа')
#     amo_Implementation_priceText3 = models.TextField(max_length=255, verbose_name='Пункт 3 тарифа')
#     amo_Implementation_priceText4 = models.TextField(max_length=255, verbose_name='Пункт 4 тарифа')
#     amo_Implementation_priceText5 = models.TextField(max_length=255, verbose_name='Пункт 5 тарифа')


#     def __str__(self):
#         return self.amo_Implementation_priceTitle

#     class Meta:
#         verbose_name = 'amoCRM | Экран с Четвертым тарифом amoCRM'
#         verbose_name_plural = 'amoCRM | Экран с Четвертым тарифом amoCRM'



# crmAdvantagesTitleLeft2 = models.CharField(max_length=255, verbose_name='Заголовок слева 2')
#     crmAdvantagesTextRight = models.TextField(max_length=255, verbose_name='Текст справа от заголовка')
#     crmAdvantagesImg3 = models.ImageField(upload_to='amopageimg/', verbose_name='Картинка слева от текста')
#     crmAdvantagesTextRight1 = models.TextField(max_length=255, verbose_name='Пункт 1 под правым заголовком')
#     crmAdvantagesTextRightdesc1 = models.TextField(max_length=255, verbose_name='Подпункт 1 под правым заголовком')
#     crmAdvantagesTexRight2 = models.TextField(max_length=255, verbose_name='Пункт 2 под правым заголовком')
#     crmAdvantagesTextRightdesc2 = models.TextField(max_length=255, verbose_name='Подпункт 2 под правым заголовком')
#     crmAdvantagesTextRight3 = models.TextField(max_length=255, verbose_name='Пункт 3 под правым заголовком')
#     crmAdvantagesTextRightdesc3 = models.TextField(max_length=255, verbose_name='Подпункт 3 под правым заголовком')
#     crmAdvantagesTextRight4 = models.TextField(max_length=255, verbose_name='Пункт 4 под правым заголовком')
#     crmAdvantagesTextRightdesc4 = models.TextField(max_length=255, verbose_name='Подпункт 4 под правым заголовком')
#     crmAdvantagesStage1 = models.CharField(max_length=255, verbose_name='Этап 1')
#     crmAdvantagesStage2 = models.CharField(max_length=255, verbose_name='Этап 2')
#     crmAdvantagesStage3 = models.CharField(max_length=255, verbose_name='Этап 3')
#     crmAdvantagesStage4 = models.CharField(max_length=255, verbose_name='Этап 4')
#     crmAdvantagesStage5 = models.CharField(max_length=255, verbose_name='Этап 5')
#     crmAdvantagesStage6 = models.CharField(max_length=255, verbose_name='Этап 6')