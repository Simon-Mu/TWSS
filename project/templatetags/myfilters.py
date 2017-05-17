# -*- coding: utf-8 -*-
from django import template

register = template.Library()


def sex_translate(value):
    if value == 'm':
        return '男'

    if value == 'f':
        return '女'

    if value == 'u':
        return '未记录'

    return ''

register.filter('sex_translate', sex_translate)
