# -*- coding: utf-8 -*-
###########################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : manage.py
#
# Creation      : 2015/12/11 16:53
# Author        : shufeng.lsf@ucweb.com
###########################################################################

import sys

from flask import render_template,request,jsonify

from flask.ext.script import Manager,Server

from mockapp.controller.views import PublicRouteController
from prestart import app
from models.mock_db import ApiInfomation

reload(sys)
sys.setdefaultencoding("utf-8")

true = True
false = False


# app.register_blueprint(format)

manager = Manager(app)
manager.add_command("runserver",Server(host="127.0.0.1",port=5000,use_reloader=False))

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/results")
def mockResult():
    return render_template('results.html')

@app.route("/apicompare")
def apiCompare():
    return render_template('apicompare.html')

@app.route("/startMock")
def startMock():
    return render_template("beginmock.html")

@app.route("/startMockDirect")
def startMockDirect():
    return render_template("beginmockdirect.html")

@app.errorhandler(404)
def pageNotFound(e):
    return render_template('404.html'),404

@app.before_request
def beforeRequest():
    request_url = request.url.split(request.url_root)[1]
    if not request_url.startswith('/'):
        request_url = '/'+request_url
    if "?" in request_url:
        request_url = request_url.split("?")[0]
    info = ApiInfomation.query.filter(ApiInfomation.api== request_url ).first()
    if info is not None:
        c = PublicRouteController(request_url)
        resp = c.redirectRoute()
        return jsonify(resp)


if __name__ == '__main__':
    manager.run()



