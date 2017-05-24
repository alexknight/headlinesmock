# -*- coding: utf-8 -*-
###########################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : mock_db.py
#
# Creation      : 2015/12/11 16:53
# Author        : shufeng.lsf@ucweb.com
###########################################################################

from datetime import datetime
import sys

from prestart import db

reload(sys)
sys.setdefaultencoding("utf-8")

class DataInfomation(db.Model):
    __tablename__ = "data_infomation"
    id = db.Column(db.Integer,primary_key=True)
    api_id = db.Column(db.Integer,db.ForeignKey("api_infomation.id"))
    data = db.Column(db.UnicodeText(4294967295))
    flag = db.Column(db.String(128))

    def __repr__(self):
       return '{"id"：%s,"api_id":"%s","data":"%s","flag":"%s"}'%(self.id,self.api_id,self.data,self.flag)

    def to_dict(self):
        return {
            'id':self.id,
            'api_id':self.api_id,
            'data':self.data,
            'flag':self.flag
        }

class ApiInfomation(db.Model):
    __tablename__ = "api_infomation"
    id = db.Column(db.Integer,primary_key=True)
    api = db.Column(db.String(255),unique=True)
    online_api = db.Column(db.TEXT)
    data_infomation = db.relationship("DataInfomation",backref="data_infomation")
    createAt = db.Column(db.DateTime,default=datetime.now())


    def __repr__(self):
        return '{"id":%s,"api":%s,"online_api":%s,"createAt":%s}' % (self.id,self.api,self.online_api,self.createAt)

    def to_dict(self):
        return {
            'id':self.id,
            'api':self.api,
            'online_api':self.online_api,
            'createAt':self.createAt
        }

if __name__ == "__main__":
    db.create_all()
