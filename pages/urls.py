from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.test_page),
    path('', views.main_page),
    path('bitrix24/', views.bitrix24_page),
    path('crm-dlya-oteley/', views.crm_dlya_oteley_page),
    path('taskflow/', views.taskflow_page),
    path('contacts/', views.contacts_page),
    path('privacy-policy/', views.privacy_policy_page),
]