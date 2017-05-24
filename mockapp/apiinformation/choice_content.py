# -*- coding: utf-8 -*-
##################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : choice_content.py
# 
# Creation      : 2015/12/18 14:24
# Author        : shufeng.lsf@ucweb.com
##################################################################
from json import JSONDecoder

def initRemoteIp(r,remoteip,result):
	info = {}
	info["login_times"]=0
	r.set(remoteip,info,ex=600)
	resp = result[0]
	return resp

def urlWithflag(r,remoteip,flagdetail):
	flag_data = flagdetail.data
	resp = JSONDecoder().decode(flag_data)
	info = eval(r.get(remoteip))
	info.pop("flag")
	r.set(remoteip,info,ex=600)
	return resp

def msgByLoginTimes(r,remoteip,result):
	info = eval(r.get(remoteip))
	times = info["login_times"]
	resp = result[times%len(result)]
	info["login_times"]+=1
	r.set(remoteip,info,ex=600)
	return resp


