# Generated by Django 3.2.7 on 2021-10-25 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_amocrmpage_crmtypes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amocrmpage_crmtypes',
            name='crmTypesRightText3',
        ),
    ]
