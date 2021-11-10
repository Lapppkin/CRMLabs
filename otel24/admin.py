from django.contrib import admin

# Register your models here.
from otel24.models import otel24page_BannerUp, otel24seoThings, setupRateOne, setupRateTwo, setupRateThree

admin.site.register(otel24page_BannerUp),
admin.site.register(otel24seoThings),
admin.site.register(setupRateOne),
admin.site.register(setupRateTwo),
admin.site.register(setupRateThree),