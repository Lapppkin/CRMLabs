from django.contrib import admin

# Register your models here.
from bitrix24.models import Bitrix24page_BannerUp, Bitrix24page_Certificate, b24seoThings

admin.site.register(Bitrix24page_BannerUp),
admin.site.register(Bitrix24page_Certificate),
admin.site.register(b24seoThings),