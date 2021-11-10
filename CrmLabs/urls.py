"""CrmLabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('test/', include('pages.urls')),
    path('bitrix24/', include('pages.urls')),
    path('crm-dlya-oteley/', include('pages.urls')),
    path('tackflow/', include('pages.urls')),
    path('contacts/', include('pages.urls')),
    path('privacy-policy/', include('pages.urls')),
    # path('test/', views.test_page),
    # path('', views.main_page),
    # path('bitrix24/', views.bitrix24_page),
    # path('crm-dlya-oteley/', views.crm_dlya_oteley_page),
    # path('tackflow/', views.tackflow_page),
    # path('contacts/', views.contacts_page),
    # path('privacy-policy/', views.privacy_policy_page),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)