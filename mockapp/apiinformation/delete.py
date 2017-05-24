# -*- coding: utf-8 -*-
#################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : editor.py
# 
# Creation      : 2015/12/20 15:50
# Author        : shufeng.lsf@ucweb.com
#################################################################

import sys

reload(sys)
sys.setdefaultencoding("utf-8")

from flask import render_template,request
from prestart import app,db
from models.mock_db import ApiInfomation,DataInfomation


@app.route('/mock/delete/<int:post_id>',methods=['GET','POST'])
def mockDelete(post_id):
    if request.method == 'GET':
        try:
            details = DataInfomation.query.filter(DataInfomation.id==post_id).first()
            db.session.delete(details)
            db.session.commit()
            apiInfo = ApiInfomation.query.filter(ApiInfomation.id==details.api_id).first()
            if len(apiInfo.data_infomation) == 0:
                db.session.delete(apiInfo)
                db.session.commit()

        except Exception:
            pass
    return render_template("results.html")