# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
BASE_DIR = os.path.dirname(os.path.abspath(__name__))
MEDIA_PATH = os.path.join(BASE_DIR, 'media')

from django.shortcuts import render


def upload(request):
    from project.utilities.check_indentity import check_identity
    check_return = check_identity(request)
    if not check_return:
        return False
    else:
        user = check_return

    # if requestfor == 'user_info':
    return upload_user_info(request, user)



def upload_user_info(request, user):
    import json
    import simplejson
    data_jsonstr = request.POST[u'request_data']

    data_json = json.loads(data_jsonstr, encoding='utf-8')

    user.phone_number = data_json[u'手机号']
    user.save()


    return render(request, 'main/utilities/return_ajax_success.html')



