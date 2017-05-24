# -*- coding: utf-8 -*-
#################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : setflag.py
# 
# Creation      : 2015/12/17 15:03
# Author        : shufeng.lsf@ucweb.com
#################################################################

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from flask import render_template,request
from prestart import app, r

'''约定:/mock/args用于设置参数,方式为/mock/args?flag=$args
'''
@app.route('/mock/args',methods=['GET'])
def setMockArgs():

    flag = request.args.get("flag","all")
    remote_ip = request.remote_addr
    info = {}
    info['flag'] = flag
    if r.exists(remote_ip):
        _info = eval(r.get(remote_ip))
        if eval(r.get(remote_ip)).has_key('login_times'):
            times = _info['login_times']
            info['login_times'] = times
            r.set(remote_ip,info,ex=600)
        else:
            info['login_times'] = 0
            r.set(remote_ip,info,ex=600)
    else:
        info['login_times'] = 0
        r.set(remote_ip,info,ex=600)

    return render_template('home.html')