# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20170521_0054'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(default='\u672a\u8bb0\u5f55', max_length=32)),
                ('session', models.IntegerField(default=0, verbose_name=128)),
                ('major', models.CharField(default='\u672a\u8bb0\u5f55', max_length=16)),
                ('credit', models.IntegerField(default=0, verbose_name=16)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lecture', to='project.User')),
            ],
        ),
    ]
