from django.contrib import admin

# Register your models here.
from .models import Header_phone
from .models import Footer_email
from .models import Footer_address_krd
from .models import Footer_address_msk

admin.site.register(Header_phone),
admin.site.register(Footer_email),
admin.site.register(Footer_address_krd),
admin.site.register(Footer_address_msk),
