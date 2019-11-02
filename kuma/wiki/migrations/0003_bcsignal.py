# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-11 09:38


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_remove_document_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='BCSignal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bc_signals', to='wiki.Document', verbose_name='Document (optional)')),
            ],
            options={
                'verbose_name': 'BC Signal',
            },
        ),
    ]
