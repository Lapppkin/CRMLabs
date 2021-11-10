from django.shortcuts import render
from headfoot.datetime import WhatYear
from headfoot.models import Header_phone, Footer_email, Footer_address_krd, Footer_address_msk
from amoCRM.models import amoCRMpage_BannerUp, amoCRMpage_BasicTerms, amoCRMpage_CrmTypes, amoCRMpage_CrmAdvantages, amoCRMpage_amo_price, amoCRMpage_amo_combo_price, amoCRMpage_amo_Implementation_price_First, amoCRMpage_amo_Implementation_price_Second, amoCRMpage_amo_Implementation_price_Third, amoCRMpage_amo_Implementation_price_Fourth, amoSeoThings
from bitrix24.models import Bitrix24page_BannerUp, Bitrix24page_Certificate, b24seoThings
from otel24.models import otel24page_BannerUp, otel24seoThings, setupRateOne, setupRateTwo, setupRateThree

# Create your views here.

# def headfoot(request):
#     phone1 = Header_phone.objects.get(pk=1)
#     Footer_email = Footer_email.objects.all()
#     Footer_address_krd = Footer_address_krd.objects.all()
#     Footer_address_msk = Footer_address_msk.objects.all()
#     return render(request, 'index_amoCRM.html', {'phone1' : phone1,})


def test_page(request):
    test_text = 'TECT PAGE'
    phone1 = Header_phone.objects.get(pk=1)
    email1 = Footer_email.objects.get(pk=1)
    address_krd1 = Footer_address_krd.objects.get(pk=1)
    address_msk1 = Footer_address_msk.objects.get(pk=1)
    now = WhatYear()
    Bitrix24page_Slider = Bitrix24page_BannerUp.objects.all()
    return render(request, 'test.html', {'test_text' : test_text,
                                        'Bitrix24page_Slider' : Bitrix24page_Slider,
                                        'phone1' : phone1,
                                        'email1' : email1,
                                        'address_krd1' : address_krd1,
                                        'address_msk1' : address_msk1,
                                        'now' : now,})


def main_page(request):
    phone1 = Header_phone.objects.get(pk=1)
    email1 = Footer_email.objects.get(pk=1)
    address_krd1 = Footer_address_krd.objects.get(pk=1)
    address_msk1 = Footer_address_msk.objects.get(pk=1)
    now = WhatYear()
    amoCRMpage_Slider = amoCRMpage_BannerUp.objects.all()
    amoCRMpage_BasicTerms_list = amoCRMpage_BasicTerms.objects.all()
    amoCRMpage_CrmTypes_list = amoCRMpage_CrmTypes.objects.all()
    amoCRMpage_CrmAdvantages_list = amoCRMpage_CrmAdvantages.objects.all()
    amoCRMpage_amo_price_list = amoCRMpage_amo_price.objects.all()
    amoCRMpage_amo_combo_price_list = amoCRMpage_amo_combo_price.objects.all()
    amoCRMpage_amo_Implementation_price_First_list = amoCRMpage_amo_Implementation_price_First.objects.all()
    amoCRMpage_amo_Implementation_price_Second_list = amoCRMpage_amo_Implementation_price_Second.objects.all()
    amoCRMpage_amo_Implementation_price_Third_list = amoCRMpage_amo_Implementation_price_Third.objects.all()
    amoCRMpage_amo_Implementation_price_Fourth_list = amoCRMpage_amo_Implementation_price_Fourth.objects.all()
    seoData = amoSeoThings.objects.all()
    return render(request, 'index_amoCRM.html', {'phone1' : phone1,
                                                'amoCRMpage_Slider' : amoCRMpage_Slider,
                                                'amoCRMpage_BasicTerms_list' : amoCRMpage_BasicTerms_list,
                                                'amoCRMpage_CrmTypes_list' : amoCRMpage_CrmTypes_list,
                                                'amoCRMpage_CrmAdvantages_list' : amoCRMpage_CrmAdvantages_list,
                                                'amoCRMpage_amo_price_list' : amoCRMpage_amo_price_list,
                                                'amoCRMpage_amo_combo_price_list' : amoCRMpage_amo_combo_price_list,
                                                'amoCRMpage_amo_Implementation_price_First_list' : amoCRMpage_amo_Implementation_price_First_list,
                                                'amoCRMpage_amo_Implementation_price_Second_list' : amoCRMpage_amo_Implementation_price_Second_list,
                                                'amoCRMpage_amo_Implementation_price_Third_list' : amoCRMpage_amo_Implementation_price_Third_list,
                                                'amoCRMpage_amo_Implementation_price_Fourth_list' : amoCRMpage_amo_Implementation_price_Fourth_list,
                                                'seoData' : seoData,
                                                'email1' : email1,
                                                'address_krd1' : address_krd1,
                                                'address_msk1' : address_msk1,
                                                'now' : now,})


def bitrix24_page(request):
    phone1 = Header_phone.objects.get(pk=1)
    email1 = Footer_email.objects.get(pk=1)
    address_krd1 = Footer_address_krd.objects.get(pk=1)
    address_msk1 = Footer_address_msk.objects.get(pk=1)
    now = WhatYear()
    Bitrix24page_BannerUp_slider = Bitrix24page_BannerUp.objects.all()
    Bitrix24page_Certificate_list = Bitrix24page_Certificate.objects.all()
    seoData = b24seoThings.objects.all()
    return render(request, 'index_bitrix24.html', {'phone1' : phone1, 
                                                    'Bitrix24page_BannerUp_slider' : Bitrix24page_BannerUp_slider,
                                                    'Bitrix24page_Certificate_list' : Bitrix24page_Certificate_list,
                                                    'seoData' : seoData,
                                                    'email1' : email1,
                                                    'address_krd1' : address_krd1,
                                                    'address_msk1' : address_msk1,
                                                    'now' : now,})


def crm_dlya_oteley_page(request):
    phone1 = Header_phone.objects.get(pk=1)
    email1 = Footer_email.objects.get(pk=1)
    address_krd1 = Footer_address_krd.objects.get(pk=1)
    address_msk1 = Footer_address_msk.objects.get(pk=1)
    now = WhatYear()
    otel24page_BannerUp_title = otel24page_BannerUp.objects.get(pk=1)
    seoData = otel24seoThings.objects.all()
    setupRateOne_list = setupRateOne.objects.all()
    setupRateTwo_list = setupRateTwo.objects.all()
    setupRateThree_list = setupRateThree.objects.all()
    return render(request, 'index_crm-dlya-oteley.html', {'phone1' : phone1,
                                                        'otel24page_BannerUp_title' : otel24page_BannerUp_title,
                                                        'seoData' : seoData,
                                                        'setupRateOne_list' : setupRateOne_list,
                                                        'setupRateTwo_list' : setupRateTwo_list,
                                                        'setupRateThree_list' : setupRateThree_list,
                                                        'email1' : email1,
                                                        'address_krd1' : address_krd1,
                                                        'address_msk1' : address_msk1,
                                                        'now' : now,})


def taskflow_page(request):
    phone1 = Header_phone.objects.get(pk=1)
    email1 = Footer_email.objects.get(pk=1)
    address_krd1 = Footer_address_krd.objects.get(pk=1)
    address_msk1 = Footer_address_msk.objects.get(pk=1)
    now = WhatYear()
    return render(request, 'index_taskflow.html', {'phone1' : phone1, 
                                                    'email1' : email1,
                                                    'address_krd1' : address_krd1,
                                                    'address_msk1' : address_msk1,
                                                    'now' : now,})


def contacts_page(request):
    phone1 = Header_phone.objects.get(pk=1)
    email1 = Footer_email.objects.get(pk=1)
    address_krd1 = Footer_address_krd.objects.get(pk=1)
    address_msk1 = Footer_address_msk.objects.get(pk=1)
    now = WhatYear()
    return render(request, 'index_contacts.html', {'phone1' : phone1, 
                                                    'email1' : email1,
                                                    'address_krd1' : address_krd1,
                                                    'address_msk1' : address_msk1,
                                                    'now' : now,})


def privacy_policy_page(request):
    phone1 = Header_phone.objects.get(pk=1)
    email1 = Footer_email.objects.get(pk=1)
    address_krd1 = Footer_address_krd.objects.get(pk=1)
    address_msk1 = Footer_address_msk.objects.get(pk=1)
    now = WhatYear()
    return render(request, 'index_privacy-policy.html', {'phone1' : phone1,
                                                        'email1' : email1,
                                                        'address_krd1' : address_krd1,
                                                        'address_msk1' : address_msk1,
                                                        'now' : now,})


