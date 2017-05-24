# -*- coding: utf-8 -*-
###########################################################################
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : format_text.py
#
# Creation      : 2015/12/11 16:53
# Author        : shufeng.lsf@ucweb.com
###########################################################################

import glob
import ConfigParser
import os
import shutil
import json
import time
from json import JSONDecoder
import sys

import requests

from prestart import app

reload(sys)
sys.setdefaultencoding("utf-8")

true = True
false =False
REG_UP = r'pullup*.json'
REG_DOWN = r'pulldown*.json'
FILES_PATH = r'%s'%os.path.abspath(os.path.join(os.path.dirname(__file__),"files"))

def configOperate(confpath):
    config = ConfigParser.ConfigParser()
    config.read(confpath)
    return config

def makeDir(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        shutil.rmtree(path)
        os.mkdir(path)


def getFileList(rootpath,reg):
    if not rootpath.endswith("/"):
        rootpath = rootpath + "/"
    new_reg = r'%s'%rootpath + '%s'%reg +'*.json'
    file_list = glob.glob(new_reg)
    return file_list


def formatFile(filelist):
    '''1.替换"为',true为True,false为False
    '''
    for file in filelist:
        app.logger.info("format file == "+file)
        src_content = readFile(file)
        content=JSONDecoder().decode(src_content)
        os.remove(file)
        writeFile(file,content)

def readFile(file):
    with open(file) as f:
        return f.read()

def writeFile(path,content):
    with open(path,'w') as file:
        file.write(json.dumps(content,ensure_ascii=False))

def requestApi(url,localpath,givename,count):
    filename = givename + "_"+str(count)+".json"
    location_name = os.path.join(localpath,filename)
    req = requests.get(url)
    content = req.json()
    writeFile(location_name,content)

def downloadFiles(files,root_path,givename,batch,delay):
    count =0
    for api in files:
        for i in range(int(batch)):
            count+=1
            requestApi(api,root_path,givename,count)
            time.sleep(int(delay))

def combineFiles(newfile,filelist):
    content_list = []
    for file in filelist:
        src_content = readFile(file)
        # src_content = src_content.replace("true","True").replace("false","False").replace("True&","true&")
        content = JSONDecoder().decode(src_content)
        content_list.append(content)
    writeFile(newfile,content_list)
    return content_list

def getDatas(apilist,batch,delay=2):
    makeDir(FILES_PATH)
    downloadFiles(apilist,FILES_PATH,givename="apiinfo",batch=batch,delay=delay)
    file_list = getFileList(FILES_PATH,"apiinfo")
    formatFile(file_list)
    combine_list = combineFiles(os.path.join(FILES_PATH,"combine.json"),file_list)
    return combine_list

def main():
    makeDir(FILES_PATH)
    app.logger.info("=====FILES_PATH====\n"+str(FILES_PATH))
    parser = configOperate(confpath="config.ini")
    pullup_api_list = eval(parser.get("API_PATH","pull_up_url"))
    pulldown_api_list = eval(parser.get("API_PATH","pull_down_url"))
    app.logger.info("***pullup_api_list length*** :"+str(len(pullup_api_list)))
    app.logger.info("***pulldown_api_list length*** :"+str(len(pulldown_api_list)))
    # 下载api内容到对应文件
    downloadFiles(pullup_api_list,FILES_PATH,givename="pullup")
    downloadFiles(pulldown_api_list,FILES_PATH,givename= "pulldown")
    pullup_file_list = getFileList(FILES_PATH,"pullup")
    pulldown_file_list= getFileList(FILES_PATH,"pulldown")
    app.logger.info("====pullup_file_list=====\n"+str(pullup_file_list))
    app.logger.info("====pulldown_file_list=====\n"+str(pulldown_file_list))
    formatFile(pullup_file_list)
    formatFile(pulldown_file_list)
    pullup_combine_list = combineFiles(os.path.join(FILES_PATH,"pullup_combine.json"),pullup_file_list)
    pulldown_combine_list = combineFiles(os.path.join(FILES_PATH,"pulldown_combine.json"),pulldown_file_list)
    app.logger.info("====pullup_combine_list=====\n"+str(pullup_combine_list))
    app.logger.info("====pulldown_combine_list=====\n"+str(pulldown_combine_list))

if __name__ == '__main__':
    main()

