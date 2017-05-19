# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
MEDIA_PATH = os.path.join(BASE_DIR, 'media')

from django.shortcuts import render


def upload(request):
    # 校验身份
    from project.utilities.check_indentity import check_identity
    check_return = check_identity(request)
    if check_return:
        user = check_return
    else:
        return False

    # 获取需求
    requestfor = request.POST['requestfor']

    if requestfor == 'user_info':
        return upload_user_info(request, user)


def upload_user_info(request, user):
    import json
    # 获取json字符串
    data_jsonstr = request.POST[u'request_data']
    # 解析为对象
    data_json = json.loads(data_jsonstr, encoding='utf-8')
    # 获取数据
    user.phone_number = data_json[u'手机号']
    # 保存
    user.save()
    # 返回成功状态
    return render(request, 'main/utilities/return_ajax_success.html')



