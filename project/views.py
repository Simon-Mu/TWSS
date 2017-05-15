# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'home.html', locals())


def login(request):
    request.encoding = 'utf-8'
    if request.POST:
        username_input = request.POST['username']
        password_input = request.POST['password']
        status_input = request.POST['status']

        # 检查是否存在此用户
        from models import User
        user_list = User.objects.filter(username=username_input)
        '''
        用filter而不是get的原因：
        当此用户不存在的时候get会报错"DoesNotExist"
        而filer只会返回一个空对象列表
        '''

        # 用户不存在
        if not user_list:
            return render(request, 'loginfailed.html')
        # 用户存在
        else:
            for user in user_list:
                # 密码错误
                if user.password != password_input:
                    return render(request, 'loginfailed.html')
                #密码正确
                else:
                    # 判断身份
                    if user.status == '教师':
                        return render(request, 'main/teacher.html')
                    elif user.status == '系负责人':
                        return render(request, 'main/dean.html')
                    elif user.status == '教务员' or '系统管理员':
                        return render(request, 'main/admin.html')
                    else:
                        return render(request, 'loginfailed.html')


    return render(request, 'loginfailed.html')