# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-02 05:13


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_squashed_0003_filter_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filter',
            options={'base_manager_name': 'objects'},
        ),
    ]
