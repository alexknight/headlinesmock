# -*- coding: utf-8 -*-
# Copyright (C) 2005-2016 UC Mobile Limited. All Rights Reserved
# File          : generate_data.py
# 
# Creation      : 2015/12/16 21:21
# Author        : shufeng.lsf@ucweb.com
#################################################################

import sys
import json
from json import JSONDecoder,JSONEncoder

from forms.mock_create import DataInformation, ApiInformation

reload(sys)
sys.setdefaultencoding("utf-8")

from flask import render_template,request, redirect,flash
from models.mock_db import ApiInfomation,DataInfomation
from prestart import app,db, csrf
from mockapp.controller.format_text import getDatas


@csrf.exempt
@app.route("/generte/data",methods=['GET','POST'])
def getOnlineData():
    '''通过在线api动态生成数据接口
    '''
    form = ApiInformation()
    # if form.validate_on_submit():
    if request.method == 'POST':
        real_api = request.form['datatextarea']
        batch = request.form['batch']
        flag = request.form['flag']
        if int(batch)>1 and flag != '':
            flash(u"多批数据不能录入一个flag")
            return render_template("beginmock.html")
        mock_api =  real_api.split("?")[0].split("iflow.uczzd.cn")[1]
        check_api = ApiInfomation.query.filter(ApiInfomation.api==mock_api).all()
        #生成接口列表
        interface_url_list = real_api.split(",")
        datas = getDatas(interface_url_list,batch=batch)
        app.logger.info(
            u"=====动态接口的提交信息：====\n"+
            "'api':%s\n'flag':%s,'datas':%s"%(mock_api,flag,str(datas))
        )
        if len(check_api)==0:
            api_infomation = ApiInfomation(
                api=mock_api,
                online_api=real_api
            )
            db.session.add(api_infomation)
            db.session.commit()
            app.logger.info(u"=====ApiInfomation信息已存入====")
        _apiInfo = ApiInfomation.query.filter(ApiInfomation.api==mock_api).first()
        api_id = _apiInfo.id

        for val in datas:
            count = 0
            info=JSONEncoder().encode(val)
            data_information = DataInfomation(
                api_id=api_id,
                data=info,
                flag=flag
            )
            db.session.add(data_information)
            db.session.commit()
            app.logger.info(
                u"=====DataInfomation第%d条信息已存入：apiInfo====\n%s"%(count,data_information)
            )
            count +=1
            data_list=[]
        #生成该接口的view
        # creator=CreateView(mock_api,api_id)
        # creator.createFile()
        app.logger.info(u"=====成功%s的生成接口：apiInfo====\n"%mock_api)
        if len(check_api)==0:
            flash(u"成功生成接口:%s"%mock_api)
        else:
            flash(u"成功新增接口数据:%s"%mock_api)
        return redirect('/')
    return render_template('beginmock.html',form=form)


@csrf.exempt
@app.route("/direct/generate/data",methods=['GET','POST'])
def directlyData():
    '''通过提交json直接生成数据接口
    '''
    form = DataInformation()
    if request.method == 'POST':
        api = form.api.data
        flag = form.flag.data
        check_api = ApiInfomation.query.filter(ApiInfomation.api==api).all()
        check_flag = DataInfomation.query.filter(DataInfomation.flag==flag).all()
        json_raw= form.datas.data
        try:
            json_data_list = json.loads(JSONDecoder().decode(json_raw))
        except Exception,e:
            app.logger.info("json数据格式错误:\n"+e.message)
            flash('json数据格式错误,请重新检查')
            return render_template("beginmockdirect.html")
        app.logger.info(
            u"=====静态接口的提交信息：====\n"+
            "'api':%s\n'flag':%s,'json_raw':%s"%(api,flag,str(json_raw))
        )
        if type(json_data_list) is list and flag != '':
            app.logger.info(u"=====多批数据不能录入一个flag====")
            flash(u"多批数据不能录入一个flag")
            return render_template("beginmockdirect.html")
        if len(check_api) == 0 and (len(check_flag) == 0 or flag==''):
            '''如果api不重复
            '''
            apiInfo = ApiInfomation(
                api=api
            )
            db.session.add(apiInfo)
            db.session.commit()
            app.logger.info(u"=====ApiInfomation信息已存入====")
            _apiInfo = ApiInfomation.query.filter(ApiInfomation.api==api).first()  #all()
            details_id = _apiInfo.id

            if type(json_data_list) is list and flag == '':
                for each in json_data_list:
                    count=1
                    json_datas = JSONEncoder().encode(each)    #each
                    apiDetail = DataInfomation(
                        api_id=details_id,
                        data=json_datas,
                        flag=flag
                    )

                    db.session.add(apiDetail)
                    db.session.commit()
                    app.logger.info(
                        u"=====DataInfomation第%d条信息已存入：apiInfo====\n%s"%(count,apiDetail)
                    )
                    count +=1
            elif type(json_data_list) is dict:
                json_datas = JSONEncoder().encode(json_data_list)
                apiDetail = DataInfomation(
                        api_id=details_id,
                        data=json_datas,
                        flag=flag
                )
                db.session.add(apiDetail)
                db.session.commit()
                app.logger.info(
                    u"=====只有一批json数据,DataInfomation信息已存入：apiInfo====\n%s"%apiDetail
                )
            # creator=CreateView(api,details_id)
            # creator.createFile()
            app.logger.info(u"=====成功%s的生成接口：apiInfo====\n"%api)
            flash(u"成功生成接口:%s"%api)
            return redirect('/')
        else:
            '''如果api重复提交,则叠加数据
            '''
            if len(check_api) != 0:
                details_id = check_api[0].id
                if type(json_data_list) is list:
                    for each in json_data_list:
                        count=1
                        json_datas = JSONEncoder().encode(each)    #each
                        apiDetail = DataInfomation(
                            api_id=details_id,
                            data=json_datas,
                            flag=flag
                        )

                        db.session.add(apiDetail)
                        db.session.commit()
                        app.logger.info(
                            u"=====DataInfomation第%d条信息已存入：apiInfo====\n%s"%(count,apiDetail)
                        )
                        count +=1
                    flash(u"存在此api,此次已追加%s批数据"%count)
                elif type(json_data_list) is dict:
                    json_datas = JSONEncoder().encode(json_data_list)
                    apiDetail = DataInfomation(
                            api_id=details_id,
                            data=json_datas,
                            flag=flag
                    )
                    db.session.add(apiDetail)
                    db.session.commit()
                    flash(u"存在此api,此次添加数据已追加")
            elif len(check_flag) != 0:
                flash(u"flag重复提交")
            return render_template("beginmockdirect.html")

    return redirect('/')