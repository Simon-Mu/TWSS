# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.


# 测试
PROJECT_TEST = True

def index(request):
    return render(request, 'index/index.html', locals())


def login(request):
    request.encoding = 'utf-8'

    # 测试
    if PROJECT_TEST:
        return render(request,'main/teacher.html')

    if request.POST:
        from models import User

        username_post = request.POST['username']
        password_post = request.POST['password']
        status_post = request.POST['status']

        # 检查是否存在此用户
        user_list = User.objects.filter(username=username_post)
        '''
        用filter而不是get的原因：
        当此用户不存在的时候get会报错"DoesNotExist"
        而filer只会返回一个空对象列表
        '''
        # 用户存在
        if user_list:
            # 遍历列表 虽然列表里只有一个对象
            for user in user_list:
                # 密码正确
                if password_post == user.password:

                    # 验证身份
                    if status_post == '教师':
                        if user.status_teacher == True:
                            return render(request, 'main/teacher.html', locals())
                    if status_post == '系负责人':
                        if user.status_dean == True:
                            return render(request, 'main/dean.html')
                    if status_post == '教务员':
                        if user.status_director == True:
                            return render(request, 'main/admin.html')
                    if status_post == '系统管理员':
                        if user.status_admin == True:
                            return render(request, 'main/admin.html')

    return render(request, 'index/loginfailed.html')






