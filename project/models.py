# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 用户表
class User(models.Model):
    # 用户名  即教工卡卡号
    username = models.CharField(max_length=12, unique=True)
    # 姓名
    name = models.CharField(max_length=10)
    # 密码 md5加密后的字符串
    password = models.CharField(max_length=32)
    # 性别
    SEX_CHOICES = (
        ('m', 'male'),
        ('f', 'female'),
        ('u', 'unknown')
    )
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default='u')
    # 身份
    STATUS_CHOICES = (
        ('0', '教师'),
        ('1', '系负责人'),
        ('2', '教务员'),
        ('3', '系统管理员')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='教师')

    class Meta:
        db_table = 'User'

    def  __unicode__(self):
        return self.username + ' ' + self.name

