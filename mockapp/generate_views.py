# -*- coding: utf-8 -*-
###########################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : generate_views.py
#
# Creation      : 2015/12/11 16:53
# Author        : shufeng.lsf@ucweb.com
###########################################################################

import os
import time

true = True
false = False
# FILE_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'mockapp\\controller\\views.py'))
FILE_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.dirname(__file__)),'mockapp/controller/views.py'))
print "FILE_PATH:\n"+FILE_PATH

class CreateView(object):

    def __init__(self,url,details_id):
        self.url = url
        self.alias = 'test_'+str(int(time.time()))
        self.details_id = details_id
        self.path = FILE_PATH

    def createFile(self):
        content = '\n\n@app.route("%s",methods=["GET"])\ndef %s():\n\tremote_ip = request.remote_addr\n\t'%(self.url,self.alias)+\
                'detail = DataInfomation.query.filter(DataInfomation.api_id==%s).all()\n\tdetail_list = []\n\t'%self.details_id+\
                'for each in detail:\n\t\tdetail_list.append(JSONDecoder().decode(each.data))\n\tresult = detail_list\n\t'+\
                'if not session.has_key(remote_ip):\n\t\tresp = initRemoteIp(session,remote_ip,result)\n\t\t'+\
                'return jsonify(resp)\n\telif session[remote_ip].has_key("flag"):\n\t\tflag = session[remote_ip]["flag"]\n\t\t'+\
                't = DataInfomation.query.filter(DataInfomation.flag==flag).all()\n\t\treg = u"/iflow/api/v1/channel"\n\t\t'+\
                'if re.search(reg, request.url_rule.rule) and len(t) > 0:\n\t\t\t'+\
                'resp = urlWithflag(session,remote_ip,t[0])\n\t\t\treturn jsonify(resp)\n\t\telse:\n\t\t\t'+\
                'resp = msgByLoginTimes(session,remote_ip,result)\n\t\t\treturn jsonify(resp)\n\t'+\
                'else:\n\t\tresp = msgByLoginTimes(session,remote_ip,result)\n\t\treturn jsonify(resp)'

        with open(self.path) as rfile:
            cont = rfile.read()
            if '@app.route("%s",methods'%self.url in cont:
                return
        with open(self.path,'a') as file:
            file.write(content)


    def createFileDirect(self):
        content = '\n\n@app.route("%s",methods=["GET"])\ndef %s():\n\tremote_ip = request.remote_addr\n\t'%(self.url,self.alias)+\
                'detail = DataInfomation.query.filter(DataInfomation.api_id==%s).all()\n\tdetail_list = []\n\t'%self.details_id+\
                'for each in detail:\n\t\tdetail_list.append(JSONDecoder().decode(each.data))\n\tresult = detail_list\n\t'+\
                'if not session.has_key(remote_ip):\n\t\tresp = initRemoteIp(session,remote_ip,result)\n\t\t'+\
                'return jsonify(resp)\n\telif session[remote_ip].has_key("flag"):\n\t\tflag = session[remote_ip]["flag"]\n\t\t'+\
                't = DataInfomation.query.filter(DataInfomation.flag==flag).all()\n\t\treg = u"/iflow/api/v1/channel"\n\t\t'+\
                'if re.search(reg, request.url_rule.rule) and len(t) > 0:\n\t\t\t'+\
                'resp = urlWithflag(session,remote_ip,t[0])\n\t\t\treturn jsonify(resp)\n\t\telse:\n\t\t\t'+\
                'resp = msgByLoginTimes(session,remote_ip,result)\n\t\t\treturn jsonify(resp)\n\t'+\
                'else:\n\t\tresp = msgByLoginTimes(session,remote_ip,result)\n\t\treturn jsonify(resp)'

        with open(self.path) as rfile:
            cont = rfile.read()
            if '@app.route("%s",methods'%self.url in cont:
                return
        with open(self.path,'a') as file:
            file.write(content)

