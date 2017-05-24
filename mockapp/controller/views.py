# -*- coding: utf-8 -*-
###########################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : views.py
#
# Creation      : 2015/12/11 16:53
# Author        : shufeng.lsf@ucweb.com
###########################################################################
import sys
import re
from json import JSONDecoder

from flask import request

from prestart import r
from models.mock_db import ApiInfomation,DataInfomation
from mockapp.apiinformation.choice_content import initRemoteIp,urlWithflag,msgByLoginTimes

reload(sys)
sys.setdefaultencoding("utf-8")


class PublicRouteController(object):
    def __init__(self,url):
        self.url = url

    def redirectRoute(self):
        try:
            remote_ip = request.remote_addr
            apiInfo  = ApiInfomation.query.filter(ApiInfomation.api==self.url).first()
            detail = DataInfomation.query.filter(DataInfomation.api_id==apiInfo.id).all()
            detail_list = []
            for each in detail:
                detail_list.append(JSONDecoder().decode(each.data))
            result = detail_list
            if not r.exists(remote_ip):
                resp = initRemoteIp(r,remote_ip,result)
                return resp
            elif eval(r.get(remote_ip)).has_key("flag"):
                flag = eval(r.get(remote_ip))["flag"]
                t = DataInfomation.query.filter(DataInfomation.flag==flag).all()
                reg = u"/iflow/api/v1/channel"
                if re.search(reg, request.url_rule.rule) and len(t) > 0:
                    resp = urlWithflag(r,remote_ip,t[0])
                    return resp
                else:
                    resp = msgByLoginTimes(r,remote_ip,result)
                    return resp
            else:
                resp = msgByLoginTimes(r,remote_ip,result)
                return resp
        except Exception as e:
            resp = {"code":404,"msg":"%s"%e}
            return resp
