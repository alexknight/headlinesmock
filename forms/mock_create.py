# -*- coding: utf-8 -*-
###########################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : mock_create.py
#
# Creation      : 2015/12/11 16:53
# Author        : shufeng.lsf@ucweb.com
###########################################################################

from flask.ext.wtf import Form
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import DataRequired


class ApiInformation(Form):
    api = StringField("api",validators=[DataRequired()])
    flag = StringField("flag",validators=[DataRequired()])
    submit = SubmitField("submit")


class DataInformation(Form):
    api = StringField("api",validators=[DataRequired()])
    flag = StringField("flag",validators=[DataRequired()])
    datas = TextAreaField("json_datas format",validators=[DataRequired()])
    submit = SubmitField("submit")
