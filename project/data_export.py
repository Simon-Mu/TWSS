# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from wsgiref.util import FileWrapper


def to_excel(request):
    unique_code = request.GET['unique_code']

    from models import User
    user_list = User.objects.filter(password=unique_code)
    if user_list:
        for user in user_list:
            name = user.name
            username = user.username

            if user.sex == 'm':
                sex = '男'
            if user.sex == 'f':
                sex = '女'
            if user.sex == 'u':
                sex = '未记录'

            status = ''
            if user.status_teacher:
                status+='教师 '
            if user.status_dean:
                status+='系负责人'
            if user.status_admin:
                status+='教务员'

    import os
    BASE_DIR = os.path.dirname(os.path.abspath(__name__))
    MEDIA_PATH = os.path.join(BASE_DIR, 'media')

    import xlwt
    import xlrd
    from xlutils.copy import copy

    workbook_template = xlrd.open_workbook(os.path.join(MEDIA_PATH, 'user_info.xls'), formatting_info=True)
    worksheet_template = workbook_template.sheet_by_index(0)

    workbook = copy(workbook_template)
    worksheet = workbook.get_sheet(0)

    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = '宋体'
    style.font = font

    worksheet.write(2, 0, username, style)
    worksheet.write(2, 1, name, style)
    worksheet.write(2, 2, sex, style)
    worksheet.write(2, 3, status, style)

    filename = os.path.join(MEDIA_PATH, name+'.xls')
    workbook.save(filename)
    wrapper = FileWrapper(file(filename))

    response = HttpResponse(wrapper)
    response['Content-Type'] = 'text/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="filename"'
    return response


