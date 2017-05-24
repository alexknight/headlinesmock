# -*- coding: utf-8 -*-
###########################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : settings.py
#
# Creation      : 2015/12/11 16:53
# Author        : shufeng.lsf@ucweb.com
###########################################################################

class Config(object):
    '''公共配置
    '''
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    '''开发配置
    '''
    DEBUG = False
    # session
    CSRF_ENABLED = True
    SECRET_KEY = "4234189"
    # online_env
    SQLALCHEMY_DATABASE_URI = "mysql://root:ucwebit@127.0.0.1/mockapp"
    # dev_env
    # SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1/apitest"
    SQLALCHEMY_ECHO = True

    REDIS_SERVER = "100.84.46.138"
    REDIS_DB = 0

config = {
    'development': DevelopmentConfig(),
}


