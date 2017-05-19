# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# 用户表
class User(models.Model):
    # 用户名  即教工卡卡号
    username = models.CharField(max_length=12, unique=True, default='未记录')
    # 姓名
    name = models.CharField(max_length=10, default=u'未记录')
    # 密码 md5加密后的字符串
    password = models.CharField(max_length=32, default=u'未记录')
    # 性别
    SEX_CHOICES = ('男', '女', '未记录')
    sex = models.CharField(max_length=3, default=u'未记录')
    # 手机号
    phone_number = models.CharField(max_length=11, default=u'未记录')
    # 身份
    STATUS_CHOICES = ('教师', '系负责人', '教务员', '系统管理员', '未记录')
    status = models.CharField(max_length=16, default=u'未记录')

    class Meta:
        # 数据表名
        db_table = 'User'

    def __unicode__(self):
        return self.username + ' ' + self.name