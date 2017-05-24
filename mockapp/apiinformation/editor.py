# -*- coding: utf-8 -*-
#################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : editor.py
# 
# Creation      : 2015/12/18 15:50
# Author        : shufeng.lsf@ucweb.com
#################################################################


import sys
from json import *
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import render_template,request, redirect,flash
from prestart import app,db
from forms.mock_create import DataInformation
from models.mock_db import DataInfomation

@app.route('/mock/editor/<int:post_id>',methods=['GET','POST'])
def mockEdit(post_id):
    # apiInfo = ApiInfomation.query.get_or_404(post_id)
    details = DataInfomation.query.filter(DataInfomation.id==post_id).first()
    form = DataInformation()
    if request.method == 'POST':
        t_flag = form.flag.data
        check = DataInfomation.query.filter(DataInfomation.flag==t_flag).all()
        #新的： len(check) is None and details.flag != t_flag
        #不变： len(check) is not None and details.flag == t_flag
        if (len(check)==0 and details.flag != t_flag) or (len(check)!= 0 and details.flag == t_flag):
            details.flag = form.flag.data
            while type(form.datas.data) is not dict:
                form.datas.data = JSONDecoder().decode(form.datas.data)
            details.data = JSONEncoder().encode(form.datas.data)
            # detail.data = form.datas.data
            db.session.commit()
            return redirect("/results")
        else:
            flash(u'警告:你提交了重复的flag!!!')
            return redirect("/mock/editor/%s"%post_id)     #如果有同个flag的处理方式
    form.id = details.id
    form.api.data = details.data_infomation.api
    if details.__dict__.has_key('flag'):
        form.flag.data = details.flag
    else:
        flag = ''
    form.datas.data = details.data
    return render_template("mockeditor.html",form=form)

