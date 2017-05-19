# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
MEDIA_PATH = os.path.join(BASE_DIR, 'media')


from django.http import HttpResponse
from wsgiref.util import FileWrapper

# TODO:




def download(request):
    from project.utilities.check_indentity import check_identity
    check_return = check_identity(request)
    if check_return == False:
        return # 返回错误信息
    else:
        user = check_return

    requestfor = request.POST['requestfor']
    if requestfor == 'user_info':
        return user_info_to_excel(request, user)


# 将user_info写入excel并返回
def user_info_to_excel(request, user):
    import xlwt
    import xlrd
    from xlutils.copy import copy

    workbook_template = xlrd.open_workbook(os.path.join(MEDIA_PATH, 'excel', 'templates','user_info.xls'), formatting_info=True)

    workbook = copy(workbook_template)
    worksheet = workbook.get_sheet(0)

    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = u'宋体'
    style.font = font

    worksheet.write(2, 0, user.username, style)
    worksheet.write(2, 1, user.name, style)
    worksheet.write(2, 2, user.sex, style)
    worksheet.write(2, 3, user.status, style)
    worksheet.write(2, 4, user.phone_number, style)

    filename = os.path.join(MEDIA_PATH, 'excel', 'user_info', user.username + '.xls')
    workbook.save(filename)
    wrapper = FileWrapper(file(filename))

    response = HttpResponse(wrapper)
    response['Content-Type'] = 'text/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="%s.xls"' % user.username
    return response
