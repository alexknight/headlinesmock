# -*- coding: utf-8 -*-
###########################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : prestart.py
#
# Creation      : 2015/12/11 16:53
# Author        : shufeng.lsf@ucweb.com
###########################################################################
'''
    加载settings.py配置,并配置app,db实例
'''
from flask import Flask
import redis
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import restful
from flask_wtf.csrf import CsrfProtect

from settings import config


# 读取所有配置
DEV_CONFIG = config['development']

# 设置
app = Flask(__name__)
api = restful.Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = DEV_CONFIG.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = DEV_CONFIG.SECRET_KEY
csrf = CsrfProtect()
csrf.init_app(app)
app.debug = DEV_CONFIG.DEBUG

db = SQLAlchemy(app)
pool = redis.ConnectionPool(host='127.0.0.1',db=0,socket_timeout=3)
r = redis.Redis(connection_pool=pool)
# session.permanent = True
# app.permanent_session_lifetime = timedelta(minutes=5)




