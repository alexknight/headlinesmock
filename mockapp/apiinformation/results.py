# -*- coding: utf-8 -*-
#################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : results.py
# 
# Creation      : 2015/12/17 19:55
# Author        : shufeng.lsf@ucweb.com
#################################################################

from flask import render_template,jsonify

from prestart import app
from models.mock_db import ApiInfomation


@app.route("/mock/api/all",methods=['GET'])
def mockApi():
    api_object = ApiInfomation.query.all()
    if api_object:
        _data = []
        info_list = []
        for each in api_object:
            data_infomation = each.data_infomation
            if each.online_api is not None:
                part_online_api = each.online_api.split("?")[0]+'...'
            else:
                part_online_api = ''
            for each_data in data_infomation:
                results = {
                	"id":each_data.id,
                    "api_id":each.id,
                	"api":each.api,
                	"part_online_api":part_online_api,
                	"online_api":each.online_api,
                    "flag":each_data.flag,
                    "createAt":"%s"%str(each.createAt)
            	}
                info_list.append(results)
        response = {"code":"succ"}
        response["data"] = info_list
        _data = []
        each_info_list = []
        app.logger.info("response:\n"+str(response))
        return jsonify(response)
    return render_template("404.html")


