# -*- coding: utf-8 -*-
from __future__ import unicode_literals


def check_identity(request):
    request.encoding = 'utf-8'

    # 接收表单数据
    username_post = request.POST['username']
    status_post = request.POST['status']
    unique_code = request.POST['unique_code']

    # 校验身份
    from project.models import User
    user_list = User.objects.filter(id=username_post)

    if user_list:
        for user in user_list:
            if user.status.find(status_post) != -1:
                from hashlib import md5
                check_unique_code_src = username_post + user.password + status_post
                generater = md5(check_unique_code_src.encode("utf8"))
                check_unique_code = generater.hexdigest()

                if unique_code == check_unique_code:
                    return user

    return False
