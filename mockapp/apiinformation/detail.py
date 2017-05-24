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
from prestart import app
from models.mock_db import DataInfomation


@app.route('/mock/detail/<int:post_id>',methods=['GET','POST'])
def mockDetail(post_id):
    if request.method == 'GET':
        details = DataInfomation.query.filter(DataInfomation.id==post_id).first()
    return render_template("mockdetail.html",details=details)