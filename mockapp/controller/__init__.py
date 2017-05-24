# -*- coding: utf-8 -*-
###########################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : views.py
#
# Creation      : 2015/12/11 16:53
# Author        : shufeng.lsf@ucweb.com
###########################################################################

from flask import Blueprint

format = Blueprint('controller',__name__,static_folder="static",template_folder="templates")
